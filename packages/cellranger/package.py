# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

import os

from spack.package import *


class Cellranger(Package):
    """Cellranger is a set of analysis pipelines that process Chromium single cell data to
    align reads, generate feature-barcode matrices, perform clustering and other secondary
    analysis, and more."""

    homepage = "https://www.10xgenomics.com/support/software/cell-ranger/latest"
    license_url = "support.10xgenomics.com/license"
    git = "https://gitlab.internal.sanger.ac.uk/ov3/cellranger"

    version("7.2.0", branch="v7.2.0")
    version("8.0.1", branch="v8.0.1")
    version("10.1.0", branch="v10.1.0")

    # cellranger is distributed as precompiled binaries that are not compatible with
    # processors without the avx instruction set ...
    conflicts("target=:k10")  # last AMD processor not to support avx
    conflicts("target=:westmere")  # last Intel processor not to support avx
    conflicts("target=:x86_64_v2")  # last generic architecture not to support avx

    def install(self, spec, prefix):
        tar = which("tar")
        tar("-xzf", f"cellranger-{self.version}.tar.gz")
        install_tree(f"cellranger-{self.version}", prefix)


    @run_after("install")
    def install_test(self):
        cellranger = Executable(join_path(self.prefix.bin, "cellranger"))
        with working_dir("spack-test", create=True):
            cellranger("--help")