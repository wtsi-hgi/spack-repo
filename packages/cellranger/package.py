# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class Cellranger(Package):
    """Cellranger is a set of analysis pipelines that process Chromium single cell data to
    align reads, generate feature-barcode matrices, perform clustering and other secondary
    analysis, and more."""

    homepage = "https://www.10xgenomics.com/support/software/cell-ranger/latest"
    url = "file:///mnt/data/softpack-agent/distfiles/cellranger-10.1.0.tar.gz"
    license("10XGenomics-SOFTWARE-EULA")

    version("10.1.0", sha256="bce72f4739f2e8193758037ff52e20b85ca716ad44e729dc748d10b25b4ccb9a")

    # cellranger is distributed as precompiled binaries that are not compatible with
    # processors without the avx instruction set ...
    conflicts("target=:k10")  # last AMD processor not to support avx
    conflicts("target=:westmere")  # last Intel processor not to support avx
    conflicts("target=:x86_64_v2")  # last generic architecture not to support avx

    def install(self, spec, prefix):
        install_tree(".", prefix)

    @run_after("install")
    def install_test(self):
        with working_dir("spack-test", create=True):
            cellranger = Executable(join_path(self.prefix.bin, "cellranger"))
            cellranger("testrun", "--help")
