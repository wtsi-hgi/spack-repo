import os

from spack.package import *


class FastLmm(Package):
    """FaST-LMM (Factored Spectrally Transformed Linear Mixed Models) is a
    program for performing genome-wide association studies (GWAS) on large
    data sets. This package installs the prebuilt binary provided by
    Microsoft Research for Linux."""

    homepage = "https://www.microsoft.com/en-us/download/details.aspx?id=52559"
    # Note: Microsoft uses a filename without a dot in the minor component
    # ("FaSTLMM.207.zip"). If Spack tries to infer URLs from a pattern it
    # may incorrectly construct "FaSTLMM.2.07.zip" and 404. To prevent this,
    # pin the exact URL on the version declaration.
    url = "https://download.microsoft.com/download/b/0/9/b095c9a0-c08b-41f7-9c7e-76097e875235/FaSTLMM.207.zip"

    # Last published on the Microsoft Download Center as v2.07
    version(
        "2.07",
        sha256="63ffb9bd6ce4b3b270c4f4b674dd8f9ac352547f2b69b8b333e43fbdccdc6606",
        url="https://download.microsoft.com/download/b/0/9/b095c9a0-c08b-41f7-9c7e-76097e875235/FaSTLMM.207.zip",
    )

    # No build toolchain: we just install the Linux binary from the archive

    def install(self, spec, prefix):
        # Install all contents under a libexec directory to keep layout intact
        install_tree(self.stage.source_path, prefix.libexec)

        # Try to locate the Linux CLI binary within the extracted tree.
        # Known names observed historically include 'fastlmmc' or 'FaSTLMM'.
        candidates = []
        for root, dirs, files in os.walk(prefix.libexec):
            for fname in files:
                low = fname.lower()
                if ("fast" in low and "lmm" in low) and not low.endswith(".exe") and not low.endswith(".bat"):
                    fpath = join_path(root, fname)
                    candidates.append(fpath)

        if not candidates:
            raise InstallError("Could not locate the FaST-LMM Linux binary in the archive")

        def score(path):
            base = os.path.basename(path)
            low = base.lower()
            s = 0
            if low == "fastlmmc":
                s -= 100  # strongest preference
            if "linux" in path.lower():
                s -= 10
            if os.access(path, os.X_OK):
                s -= 5
            # prefer shorter/shallower names
            s += len(path.split(os.sep))
            s += len(base)
            return s

        candidates.sort(key=score)
        binary_path = candidates[0]

        # Ensure it is executable and install to prefix.bin
        mkdirp(prefix.bin)
        dest = join_path(prefix.bin, os.path.basename(binary_path))
        install(binary_path, dest)
        set_executable(dest)

    @run_after("install")
    def install_test(self):
        # Validate the CLI by invoking help and asserting the banner appears.
        # Do not suppress errors via fail_on_error=False; instead, capture and inspect.
        import subprocess

        bin_dir = join_path(self.prefix, "bin")
        names = ["fastlmmc", "fastlmm", "FaSTLMM", "FaSTLmm"]

        candidates = []
        for name in names:
            path = join_path(bin_dir, name)
            if os.path.exists(path):
                candidates.append(path)
        if not candidates and os.path.isdir(bin_dir):
            for fname in sorted(os.listdir(bin_dir)):
                fpath = join_path(bin_dir, fname)
                if os.path.isfile(fpath) and (os.stat(fpath).st_mode & 0o111):
                    candidates.append(fpath)

        if not candidates:
            raise InstallError("FaST-LMM CLI not found in bin directory")

        # Use the first candidate and run '-help'
        cli = candidates[0]
        res = subprocess.run([cli, "-help"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        combined = (res.stdout or b"") + b"\n" + (res.stderr or b"")
        text = combined.decode("utf-8", errors="ignore")
        # Accept as valid if the well-known banner string appears
        if "FaSTLmm" not in text and "Factored Spectrally Transformed Linear Mixed" not in text:
            raise InstallError("FaST-LMM help text not detected; output was: {}".format(text[:300]))
