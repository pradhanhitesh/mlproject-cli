FRAMEWORK_REQUIREMENTS = {
    "tensorflow": {
        "linux": [
            "tensorflow==2.15.0"
        ],
        "darwin": [
            "tensorflow-macos==2.15.0"
        ],
    },
    "keras": {
        "linux": [
            "keras==3.3.0"
        ],
        "darwin": [
            "keras==3.3.0"
        ],
    },
    "torch": {
        "linux": [
            "torch==2.1.2",
            "torchvision==0.16.2",
            "torchaudio==2.1.2"
        ],
        "darwin": [
            "# To install PyTorch on macOS (CPU only, nightly):"
            "pip3 install --pre torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/nightly/cpu"
        ],
    },
}