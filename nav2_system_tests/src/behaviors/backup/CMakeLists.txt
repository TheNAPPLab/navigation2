<<<<<<< HEAD
nav2_add_test(test_backup_behavior
=======
ament_add_test(test_backup_behavior
>>>>>>> jazzy
  GENERATE_RESULT_FOR_RETURN_CODE_ZERO
  COMMAND "${CMAKE_CURRENT_SOURCE_DIR}/test_backup_behavior.launch.py"
  WORKING_DIRECTORY "${CMAKE_CURRENT_BINARY_DIR}"
  TIMEOUT 60
  ENV
    TEST_DIR=${CMAKE_CURRENT_SOURCE_DIR}
)
