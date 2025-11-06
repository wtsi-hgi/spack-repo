# Copyright 2013-2025 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os
from spack.package import *


class FastLmm(Package):
    """FaST-LMM (Factored Spectrally Transformed Linear Mixed Models) is a
    program for performing genome-wide association studies (GWAS) on large
    data sets. This package installs the prebuilt Linux binary distributed by
    Microsoft Research."""

    homepage = "https://www.microsoft.com/en-us/download/details.aspx?id=52559"
    # Provide a default URL but specify exact URL in version() to avoid
    # incorrect version templating on the nonstandard filename.
    url = "https://download.microsoft.com/download/b/0/9/b095c9a0-c08b-41f7-9c7e-76097e875235/FaSTLMM.207.zip"

    maintainers("wtsi-hgi")

    # The archive includes a prebuilt, statically linked Linux x86_64 binary
    version(
        "2.07",
        sha256="63ffb9bd6ce4b3b270c4f4b674dd8f9ac352547f2b69b8b333e43fbdccdc6606",
        url="https://download.microsoft.com/download/b/0/9/b095c9a0-c08b-41f7-9c7e-76097e875235/FaSTLMM.207.zip",
    )

    # Only distributed with a Linux x86_64 binary
    conflicts("platform=darwin", msg="FaST-LMM binary is only provided for Linux")
    conflicts("target=aarch64:", msg="FaST-LMM binary is x86_64-only")

    def install(self, spec, prefix):
        src = self.stage.source_path

        # Install the prebuilt CLI
        bin_path = join_path(src, "Bin", "Linux_MKL", "fastlmmc")
        mkdirp(prefix.bin)
        dest = prefix.bin.fastlmmc
        install(bin_path, dest)
        os.chmod(dest, 0o755)

        # Install the rest of the archive under share for reference (docs, tests)
        install_tree(src, prefix.share.fast_lmm)

        # Duplicate key docs in a standard docs dir
        for docname in ("README.TXT", "LICENSE.TXT", "NOTICE.TXT"):
            docpath = join_path(src, docname)
            if os.path.exists(docpath):
                mkdirp(prefix.share.doc)
                install(docpath, prefix.share.doc)

        manual = join_path(src, "Doc", "user-manual.pdf")
        if os.path.exists(manual):
            mkdirp(prefix.share.doc)
            install(manual, prefix.share.doc)

    @run_after("install")
    def install_test(self):
        # Basic CLI presence and help check
        with working_dir("spack-test", create=True):
            exe = Executable(join_path(self.prefix.bin, "fastlmmc"))
            exe("-h", fail_on_error=False)
