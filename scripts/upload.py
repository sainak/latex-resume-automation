import argparse
from pathlib import Path

from google.oauth2 import service_account
from google.auth.exceptions import GoogleAuthError
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload


def upload_basic(folder_id: str, credentials_path: Path, file_path: Path) -> str:
    try:
        credentials = service_account.Credentials.from_service_account_file(
            str(credentials_path),
            scopes=("https://www.googleapis.com/auth/drive",),
        )
        service = build("drive", "v3", credentials=credentials)

        filename = file_path.name
        file_metadata = {
            "name": filename,
            "parents": [folder_id],
        }
        media = MediaFileUpload(str(file_path), mimetype="application/pdf")

        previous_file = (
            service.files()
            .list(
                q=f"'{folder_id}' in parents and name = '{filename}'",
                pageSize=1,
                fields="files(id, name)",
            )
            .execute()
        )
        try:
            file_id = previous_file["files"][0]["id"]
            file_metadata.pop("parents")
            # pylint: disable=maybe-no-member
            file = (
                service.files()
                .update(
                    fileId=file_id,
                    body=file_metadata,
                    media_body=media,
                    fields="id",
                )
                .execute()
            )
        except (IndexError, KeyError):
            # pylint: disable=maybe-no-member
            file = (
                service.files()
                .create(
                    body=file_metadata,
                    media_body=media,
                    fields="id",
                )
                .execute()
            )
        return file.get("id")
    except (GoogleAuthError, HttpError) as error:
        print(f"An error occurred: {error}")
        exit(-1)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("folder_id")
    parser.add_argument("credentials_path")
    parser.add_argument("file_path")
    args = parser.parse_args()

    file_id = upload_basic(
        args.folder_id,
        Path(args.credentials_path).resolve(),
        Path(args.file_path).resolve(),
    )

    print(f"https://drive.google.com/uc?id={file_id}")


if __name__ == "__main__":
    main()
