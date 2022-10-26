# 安装

参考：https://gocv.io/getting-started/macos/

# 摄像头启动命令

- go get -u -d gocv.io/x/gocv
- brew upgrade opencv
- brew install opencv
- brew install pkgconfig
- go run ./cmd/version/main.go

# 人脸识别

- brew install tbb numpy vtk
- brew install opencv
- go run face-detect.go 0 data/haarcascade_frontalface_default.xml

## 参考：

- https://gocv.io/writing-code/face-detect/
- https://github.com/hybridgroup/gocv/tree/release/cmd

# BUG

```bash
==> Pouring opencv--4.6.0.arm64_monterey.bottle.tar.gz
Error: The `brew link` step did not complete successfully
The formula built, but is not symlinked into /opt/homebrew
Could not symlink lib/python3.10/site-packages/cv2/__init__.py
Target /opt/homebrew/lib/python3.10/site-packages/cv2/__init__.py
already exists. You may want to remove it:
  rm '/opt/homebrew/lib/python3.10/site-packages/cv2/__init__.py'

To force the link and overwrite all conflicting files:
  brew link --overwrite opencv

To list all files that would be deleted:
  brew link --overwrite --dry-run opencv

Possible conflicting files are:
/opt/homebrew/lib/python3.10/site-packages/cv2/__init__.py
/opt/homebrew/lib/python3.10/site-packages/cv2/config.py
/opt/homebrew/lib/python3.10/site-packages/cv2/gapi/__init__.py
/opt/homebrew/lib/python3.10/site-packages/cv2/load_config_py2.py
/opt/homebrew/lib/python3.10/site-packages/cv2/load_config_py3.py
/opt/homebrew/lib/python3.10/site-packages/cv2/mat_wrapper/__init__.py
/opt/homebrew/lib/python3.10/site-packages/cv2/misc/__init__.py
/opt/homebrew/lib/python3.10/site-packages/cv2/misc/version.py
/opt/homebrew/lib/python3.10/site-packages/cv2/utils/__init__.py
==> Summary
🍺  /opt/homebrew/Cellar/opencv/4.6.0: 855 files, 120.3MB
==> Running `brew cleanup opencv`...
Disable this behaviour by setting HOMEBREW_NO_INSTALL_CLEANUP.
Hide these hints with HOMEBREW_NO_ENV_HINTS (see `man brew`).
```
