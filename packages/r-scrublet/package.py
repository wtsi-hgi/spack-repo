# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScrublet(RPackage):
    """R Interface to Python's Scrublet Package for Detecting Doublets in Single-Cell Data.

    Provides an R interface to run Scrublet, a Python package for detecting doublets
    in single-cell RNA-seq data. The package allows both one-step and step-by-step
    doublet detection workflows."""

    homepage = "https://github.com/Moonerss/scrubletR"
    url = "https://github.com/Moonerss/scrubletR/archive/refs/heads/master.tar.gz"
    git = "https://github.com/Moonerss/scrubletR.git"

    version("0.2.0", commit="1c08e58c7a551406819263603161d49e3055effc")

    # R dependencies from DESCRIPTION file
    depends_on("r-ggplot2", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-patchwork", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-scales", type=("build", "run"))
    depends_on("r-seurat", type=("build", "run"))

    # Python dependencies
    depends_on("py-scrublet", type=("build", "run"))
    depends_on("python@3.7:", type=("build", "run"))
