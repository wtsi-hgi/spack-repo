# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSangerseqr(RPackage):
    """Tools for Sanger Sequencing Data in R

    This package contains several tools for analyzing Sanger Sequencing data files in R, including reading .scf and .ab1 files, making basecalls and plotting chromatograms.
    """

    bioc = "sangerseqR"

    version("1.44.0", commit="64db9d2b0d841c5d8dd0336329ceedc91f975d96")
    version("1.38.0", commit="c460464a3f73eefd77a5ffc44e3d58d4204443c1")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-pwalign", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-shiny", type=("build", "run"))
