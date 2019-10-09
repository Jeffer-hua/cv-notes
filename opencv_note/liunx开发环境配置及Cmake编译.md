#### env : Ubuntu18.04,OpenCV4.1.1
1. [OpenCV-Releases](https://opencv.org/releases/),选择自己需要的版本，点击Source下载
2. 安装cmake及其依赖项
```bash
sudo apt-get update
sudo apt-get install cmake
sudo apt-get install build-essential libgtk2.0-dev libavcodec-dev libavformat-dev libjpeg.dev libtiff4.dev libswscale-dev libjasper-dev
```
3. Cmake编译
```bash
# 解压下载好的压缩包
unzip opencv-4.1.1.zip
# 创建编译文件夹并进入
cd opencv-4.1.1
mkdir build
cd bulid 
# cmake
cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
# 编译 
sudo make
# 安装 
sudo make install 
```
4. 配置环境变量
```bash
sudo vim /etc/ld.so.conf.d/opencv.conf 
# 在最添加以下内容 
# /usr/local/lib 
# 执行命令使对上面的修改生效
sudo ldconfig
# 配置bash
sudo vim /etc/bash.bashrc
# 在最添加以下内容
# PKG_CONFIG_PATH=$PKG_CONFIG_PATH:/usr/local/lib/pkgconfig  
# export PKG_CONFIG_PATH
# 使得配置生效
source /etc/bash.bashrc 
sudo updatedb
```
5. 测试
```bash
# 进入OpenCV自带cmake demo
cd opencv-4.1.1/samples/cpp/example_cmake
# 编译成可执行程序
cmake .
make
# 运行打开摄像头Demo 
./opencv_example
```
---
- CMakeLists.txt
```bash
# cmake needs this line
cmake_minimum_required(VERSION 3.1)

# Enable C++11
set(CMAKE_CXX_STANDARD 11)
set(CMAKE_CXX_STANDARD_REQUIRED TRUE)

# Define project name 需要修改的项目名
project(DisplayImage)

# Find OpenCV, you may need to set OpenCV_DIR variable
# to the absolute path to the directory containing OpenCVConfig.cmake file
# via the command line or GUI
find_package(OpenCV REQUIRED)

# If the package has been found, several variables will
# be set, you can find the full list with descriptions
# in the OpenCVConfig.cmake file.
# Print some message showing some of them
message(STATUS "OpenCV library status:")
message(STATUS "    config: ${OpenCV_DIR}")
message(STATUS "    version: ${OpenCV_VERSION}")
message(STATUS "    libraries: ${OpenCV_LIBS}")
message(STATUS "    include path: ${OpenCV_INCLUDE_DIRS}")

# Declare the executable target built from your sources
# 需要修改的生成可执行文件的项目名，以及源程序
add_executable(DisplayImage test.cpp)

# Link your application with OpenCV libraries
# 需要修改的可执行程序名
target_link_libraries(DisplayImage LINK_PRIVATE ${OpenCV_LIBS})
```