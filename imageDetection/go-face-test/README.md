# 安装及操作步骤

- brew install dlib
- mkdir go-face-test
- cd go-face-test && git clone https://github.com/Kagami/go-face-testdata testdata

# BUG (can't run on macos m1)

## clang: error: the clang compiler does not support '-march=native'

- https://github.com/Kagami/go-face/issues/86
- https://stackoverflow.com/questions/65966969/why-does-march-native-not-work-on-apple-m1

## classify.cc:2:10: fatal error: 'dlib/graph_utils.h' file not found

- https://githublab.com/repository/issues/Kagami/go-face/71