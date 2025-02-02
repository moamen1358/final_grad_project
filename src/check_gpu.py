import onnxruntime as ort

# Check available providers
print(ort.get_available_providers())
# Expected output: ['CUDAExecutionProvider', 'CPUExecutionProvider', ...]