# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSepstratifier(RPackage):
    """Stratification of infectious disease patients by gene expression profile."""

    homepage = "https://github.com/jknightlab/SepstratifieR"
    url = "https://github.com/jknightlab/SepstratifieR/archive/refs/tags/v1.0.0.tar.gz"
    git = "https://github.com/jknightlab/SepstratifieR.git"

    license("MIT")

    version("1.0.0", sha256="d09a106efc44f60df298547296e3809d8ac4d87c079a82a03d01dafeb943f244")

    depends_on("r@3.5.0:", type=("build", "run"))

    with default_args(type=("build", "run")):
        depends_on("r-devtools")
        depends_on("r-biocmanager")
        depends_on("r-batchelor")
        depends_on("r-matrixgenerics")
        depends_on("r-caret")
        depends_on("r-randomforest")
        depends_on("r-dplyr")
        depends_on("r-ggplot2")
        depends_on("r-pheatmap")
