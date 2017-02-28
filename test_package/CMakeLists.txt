project (LemonTest)
cmake_minimum_required(VERSION 2.8)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()
LIST(APPEND CMAKE_PROGRAM_PATH ${CONAN_BIN_DIRS}) 
FIND_PROGRAM(lemon_var lemon)
MESSAGE(${CMAKE_CURRENT_BINARY_DIR})

add_custom_target(gen
    ${lemon_var} test.y
    )
