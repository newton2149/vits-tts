import argparse



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Whisper App Arguments")
    parser.add_argument("--perform_vad", type=bool, default=False, help="Perform VAD")
    parser.add_argument("--force_align", type=bool, default=False, help="Force Align")
    parser.add_argument("--diarize", type=bool, default=False, help="Diarize")
    parser.add_argument("--min_speakers", type=int, default=1, help="Minimum number of speakers")
    parser.add_argument("--max_speakers", type=int, default=4, help="Maximum number of speakers")
    parser.add_argument("--model_size", type=str, default="tiny.en", help="Model size")
    parser.add_argument("--device", type=str, default="cuda", help="Device")
    parser.add_argument("--compute_type", type=str, default="int8", help="Compute type")
    parser.add_argument("--output_format", type=str, default="json", help="Output format")
    parser.add_argument("--input_path", type=str, default="file.zip", help="Input path")

    args = parser.parse_args()

    print("Perform VAD:", args.perform_vad)
    print("Force Align:", args.force_align)
    print("Diarize:", args.diarize)
    print("Min Speakers:", args.min_speakers)
    print("Max Speakers:", args.max_speakers)
    print("Model Size:", args.model_size)
    print("Device:", args.device)
    print("Compute Type:", args.compute_type)
    print("Output Format:", args.output_format)
    print("Input Path:", args.input_path)

