from libs.transcript_processor.transcript_file import TranscriptFile
from libs.transcript_processor.whisper_processor import WhisperProcessor


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Transcription rest api")
    parser.add_argument(
        "-p",
        "--port",
        type=str,
        required=False,
        help="""Specifies the port number listen on (e.g., 8080, 5000).
        This option defaults to a randomly assigned port if not provided.""",
    )
    parser.add_argument(
        "-H",
        "--host",
        type=str,
        required=False,
        default="0.0.0.0",
        help="""Specifies the host on which to bind (e.g., 127.0.0.1, ::).
        Defaults to 0.0.0.0 if not provided.""",
    )
    parser.add_argument("-ll", "--log-level", required=False, help="Specifies the log level (e.g., INFO, WARNING)")
    args = parser.parse_args()

    processor = WhisperProcessor(model_name="small")
    _, segments = processor.process_audio(args.input)
    writer = TranscriptFile(args.output)
    writer.write_segments_to_json(segments)


if __name__ == "__main__":
    main()