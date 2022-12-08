package main

import (
	"fmt"
	"image/color"
	"log"

	"github.com/Kagami/go-face"
	"gocv.io/x/gocv"
)

const dataDir = "testdata"

// testdata 目录下两个对应的文件夹目录
const (
	modelDir  = dataDir + "/models"
	imagesDir = dataDir + "/images"
)

// 图片中的人名
var labels = []string{
	"萧敬腾",
	"周杰伦",
	"unknow",
	"王力宏",
	"陶喆",
	"林俊杰",
}

func main() {
	// 初始化识别器
	rec, err := face.NewRecognizer(modelDir)
	if err != nil {
		fmt.Println("Cannot INItialize recognizer")
	}
	defer rec.Close()

	fmt.Println("Recognizer Initialized")

	// 调用该方法，传入路径。返回面部数量和任何错误
	faces, err := rec.RecognizeFile("heyin.jpeg")
	if err != nil {
		log.Fatalf("无法识别: %v", err)
	}
	// 打印人脸数量
	fmt.Println("图片人脸数量: ", len(faces))

	var samples []face.Descriptor
	var peoples []int32
	for i, f := range faces {
		samples = append(samples, f.Descriptor)
		// 每张脸唯一 id
		peoples = append(peoples, int32(i))
	}

	// Pass samples to the recognizer.
	rec.SetSamples(samples, peoples)

	RecognizePeople(rec, "jay.jpeg")
	RecognizePeople(rec, "linjunjie.jpeg")
	RecognizePeople(rec, "taozhe.jpeg")

	// set to use a video capture device 0
	deviceID := 0

	// open webcam
	webcam, err := gocv.OpenVideoCapture(deviceID)
	if err != nil {
		fmt.Println(err)
		return
	}
	defer webcam.Close()

	// open display window
	window := gocv.NewWindow("Face Detect")
	defer window.Close()

	// prepare image matrix
	img := gocv.NewMat()
	defer img.Close()

	// color for the rect when faces detected
	blue := color.RGBA{0, 0, 255, 0}

	// load classifier to recognize faces
	classifier := gocv.NewCascadeClassifier()
	defer classifier.Close()

	if !classifier.Load("./haarcascade_frontalface_default.xml") {
		fmt.Println("Error reading cascade file: data/haarcascade_frontalface_default.xml")
		return
	}

	fmt.Printf("start reading camera device: %v\n", deviceID)
	for {
		if ok := webcam.Read(&img); !ok {
			fmt.Printf("cannot read device %v\n", deviceID)
			return
		}
		if img.Empty() {
			continue
		}

		// detect faces
		rects := classifier.DetectMultiScale(img)
		if len(rects) == 0 {
			continue
		}

		fmt.Printf("found %d faces\n", len(rects))

		// draw a rectangle around each face on the original image
		for _, r := range rects {
			gocv.Rectangle(&img, r, blue, 3)

			imgFace := img.Region(r)
			buff, err := gocv.IMEncode(".jpg", imgFace)
			if err != nil {
				fmt.Println("encoding to jpg err:%v", err)
				break
			}

			RecognizePeopleFromMemory(rec, buff)
		}

		// show the image in the window, and wait 1 millisecond
		window.IMShow(img)
		window.WaitKey(1)
	}
}

func RecognizePeople(rec *face.Recognizer, file string) {
	people, err := rec.RecognizeSingleFile(file)
	if err != nil {
		log.Fatalf("无法识别: %v", err)
	}
	if people == nil {
		log.Fatalf("图片上不是一张脸")
	}
	peopleID := rec.Classify(people.Descriptor)
	if peopleID < 0 {
		log.Fatalf("无法区分")
	}
	fmt.Println(peopleID)
	fmt.Println(labels[peopleID])
}

func RecognizePeopleFromMemory(rec *face.Recognizer, img []byte) {
	people, err := rec.RecognizeSingle(img)
	if err != nil {
		log.Println("无法识别: %v", err)
		return
	}
	if people == nil {
		log.Println("图片上不是一张脸")
		return
	}
	peopleID := rec.Classify(people.Descriptor)
	if peopleID < 0 {
		log.Println("无法区分")
		return
	}
	fmt.Println(peopleID)
	fmt.Println(labels[peopleID])
}
