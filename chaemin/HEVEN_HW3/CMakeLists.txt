cmake_minimum_required(VERSION 3.8)
project(tutorial)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# 🔥 필요한 패키지 찾기
find_package(ament_cmake REQUIRED)
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# 🔥 msg 생성
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/FirstMsg.msg"
  "msg/SecondMsg.msg"
  DEPENDENCIES builtin_interfaces std_msgs
)

# 🔥 파이썬 노드 설치
install(PROGRAMS
  src/start_node.py
  src/middle_node.py
  src/end_node.py
  DESTINATION lib/${PROJECT_NAME}
)

# 🔥 launch 폴더 설치
install(DIRECTORY launch
  DESTINATION share/${PROJECT_NAME}
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  set(ament_cmake_copyright_FOUND TRUE)
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
