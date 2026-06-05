# Route planner benchmarking script
add_executable(performance_benchmarking performance_benchmarking.cpp)
target_link_libraries(performance_benchmarking
  ${library_name}
)
install(TARGETS
  performance_benchmarking
  RUNTIME DESTINATION lib/${PROJECT_NAME}
)

# Test utilities and basic types
<<<<<<< HEAD
nav2_add_gtest(test_utils_and_types
=======
ament_add_gtest(test_utils_and_types
>>>>>>> jazzy
  test_utils_and_types.cpp
)
target_link_libraries(test_utils_and_types
  ${library_name}
)

# Test edge scorer + plugins
<<<<<<< HEAD
nav2_add_gtest(test_edge_scorers
=======
ament_add_gtest(test_edge_scorers
>>>>>>> jazzy
  test_edge_scorers.cpp
)
target_link_libraries(test_edge_scorers
  ${library_name} edge_scorers
)

# Test path converter
<<<<<<< HEAD
nav2_add_gtest(test_path_converter
=======
ament_add_gtest(test_path_converter
>>>>>>> jazzy
  test_path_converter.cpp
)
target_link_libraries(test_path_converter
  ${library_name}
)

# Test node spatial tree
<<<<<<< HEAD
nav2_add_gtest(test_spatial_tree
=======
ament_add_gtest(test_spatial_tree
>>>>>>> jazzy
  test_spatial_tree.cpp
)
target_link_libraries(test_spatial_tree
  ${library_name}
)

# Test operation manager + plugins
<<<<<<< HEAD
nav2_add_gtest(test_operations
=======
ament_add_gtest(test_operations
>>>>>>> jazzy
  test_operations.cpp
)
target_link_libraries(test_operations
  ${library_name} route_operations
)

# Test graph loader
<<<<<<< HEAD
nav2_add_gtest(test_graph_loader
=======
ament_add_gtest(test_graph_loader
>>>>>>> jazzy
    test_graph_loader.cpp
)
target_link_libraries(test_graph_loader
    ${library_name}
)

# Test graph saver
<<<<<<< HEAD
nav2_add_gtest(test_graph_saver
=======
ament_add_gtest(test_graph_saver
>>>>>>> jazzy
    test_graph_saver.cpp
)
target_link_libraries(test_graph_saver
    ${library_name}
)

# Test geojson parser
<<<<<<< HEAD
nav2_add_gtest(test_geojson_graph_file_loader
=======
ament_add_gtest(test_geojson_graph_file_loader
>>>>>>> jazzy
    test_geojson_graph_file_loader.cpp
)
target_link_libraries(test_geojson_graph_file_loader
  ${library_name} graph_file_loaders
)

# Test geojson saver
<<<<<<< HEAD
nav2_add_gtest(test_geojson_graph_file_saver
=======
ament_add_gtest(test_geojson_graph_file_saver
>>>>>>> jazzy
    test_geojson_graph_file_saver.cpp
)
target_link_libraries(test_geojson_graph_file_saver
  ${library_name} graph_file_loaders graph_file_savers
)

# Test collision monitor separately due to relative complexity
<<<<<<< HEAD
nav2_add_gtest(test_collision_operation
=======
ament_add_gtest(test_collision_operation
>>>>>>> jazzy
  test_collision_operation.cpp
)
target_link_libraries(test_collision_operation
  ${library_name} route_operations
)

# Test route planner
<<<<<<< HEAD
nav2_add_gtest(test_route_planner
=======
ament_add_gtest(test_route_planner
>>>>>>> jazzy
  test_route_planner.cpp
)
target_link_libraries(test_route_planner
  ${library_name} edge_scorers
)

# Test goal intent extractor
<<<<<<< HEAD
nav2_add_gtest(test_goal_intent_extractor
=======
ament_add_gtest(test_goal_intent_extractor
>>>>>>> jazzy
  test_goal_intent_extractor.cpp
)
target_link_libraries(test_goal_intent_extractor
  ${library_name}
)

# Test route tracker
<<<<<<< HEAD
nav2_add_gtest(test_route_tracker
=======
ament_add_gtest(test_route_tracker
>>>>>>> jazzy
  test_route_tracker.cpp
)
target_link_libraries(test_route_tracker
  ${library_name}
)

# Test route server
<<<<<<< HEAD
nav2_add_gtest(test_route_server
=======
ament_add_gtest(test_route_server
>>>>>>> jazzy
  test_route_server.cpp
)
target_link_libraries(test_route_server
  ${library_name}
)

# Test goal intent search
<<<<<<< HEAD
nav2_add_gtest(test_goal_intent_search
=======
ament_add_gtest(test_goal_intent_search
>>>>>>> jazzy
  test_goal_intent_search.cpp
)
target_link_libraries(test_goal_intent_search
  ${library_name}
)

# Test corner smoothing
<<<<<<< HEAD
nav2_add_gtest(test_corner_smoothing
=======
ament_add_gtest(test_corner_smoothing
>>>>>>> jazzy
  test_corner_smoothing.cpp
)
target_link_libraries(test_corner_smoothing
  ${library_name}
)
