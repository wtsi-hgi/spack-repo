# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class CellrangerArc(Package):
    """Cell Ranger ARC is an advanced analytical suite designed for the Chromium Single Cell Multiome ATAC + Gene Expression sequencing. It provides in-depth analysis of gene expression and chromatin accessibility at a single cell level, uniquely linking these aspects for enhanced genomic understanding."""

    homepage = "https://www.10xgenomics.com/support/software/cell-ranger-arc/latest"
    license_url = "support.10xgenomics.com/license"
    git = "https://gitlab.internal.sanger.ac.uk/eh19/cellranger.git"

    version("2.0.2", branch="arc-2.0.2")

    # cellranger is distributed as precompiled binaries that are not compatible with
    # processors without the avx instruction set ...
    conflicts("target=:k10")  # last AMD processor not to support avx
    conflicts("target=:westmere")  # last Intel processor not to support avx
    conflicts("target=:x86_64_v2")  # last generic architecture not to support avx

    def install(self, spec, prefix):
        tar = which("tar")
        tar("-xzf", f"cellranger-arc-{self.version}.tar.gz")
        install_tree(f"cellranger-arc-{self.version}", prefix)
