"""
zip_packager.py
Generates a zip containing a target folder's files, folders, subfolders, etc
Provides additional tools for interacting with packaged zips
Creates a manifest.txt at *.zip://manifest.txt
Creates a manifest.json file at *.zip://manifest.json
"""
import os, io, json, zipfile
from os.path import abspath, basename, dirname, exists, isdir, relpath, splitext


def package_folder(
    path: str,
    out: str,
    name: str = None,
    endings: list = None,
    exclude: list = None,
) -> str:
    path, out = abspath(path), abspath(out)
    out = out.strip(".zip")
    name = name or splitext(basename(out))[0]
    if not isdir(dirname(out)):
        raise NotADirectoryError(f"Zip output directory does not exist.")

    if not isdir(path):
        raise NotADirectoryError(
            f"Package function path must be a valid, non-empty folder."
        )
    with zipfile.ZipFile(
        zipfile_data := io.BytesIO(),
        "w",
        compresslevel=9,
        compression=zipfile.ZIP_DEFLATED,
    ) as z:
        manifest = []

        def _package(parent: str):
            for p in os.scandir(parent):
                if p.is_dir():  # Recursive case
                    _package(p.path)
                else:
                    if exclude and p in exclude:
                        continue
                    if endings and not any(p.path.endswith(end) for end in endings):
                        continue
                    z.write(rel := relpath(p.path, start=path))
                    manifest.append(rel)

        _package(path)
        z.writestr(zipfile.ZipInfo("manifest.txt"), "\n".join(manifest))
        z.writestr(
            zipfile.ZipInfo("manifest.json"),
            json.dumps(
                {
                    "name": name,
                    "file_count": len(manifest),
                    "manifest": manifest,
                },
                indent=4,
            ),
        )
    with open(outfile := out + ".zip", "wb+") as f:
        f.write(zipfile_data.getvalue())
    print(f"{name} manifest: {manifest}")
    print(f"Wrote {name} to {outfile} - {len(manifest)} files. ")
    return outfile


def get_package_file(path: str, file: str, mode="r") -> str:
    """Can take a file / list of files and returns the loaded file / list of files appropriately."""
    with zipfile.ZipFile(path, "r") as z:
        if isinstance(file, str):
            with z.open(file, mode) as f:
                data = f.read()
                return data.decode() if mode == "r" else data
        elif isinstance(file, list):
            files = []
            for f in file:
                with z.open(f, mode) as f:
                    data = f.read()
                    files.append(data.decode() if mode == "r" else data)
            return files


def get_package_manifest(path: str) -> list:
    """Get's a package's manifest file as a list"""
    return get_package_file(path, "manifest.txt").splitlines()


def get_package_manifest_json(path: str) -> dict:
    """Get's a package's manifest json data as a dict"""
    return json.loads(get_package_file(path, "manifest.json"))


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Directory to package", type=str)
    parser.add_argument("out", help="Output file path", type=str)
    args = parser.parse_args()
    package(args.path, args.out)
