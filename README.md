# Install Bazel via Homebrew

https://bazel.build/install/os-x#step_2_install_bazel_via_homebrew

# Run tests

```bash
bazel test //src/calculator/...
```

# Build and run FastAPI service

```bash
bazel run //src/web:main_image
```