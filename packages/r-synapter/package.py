# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSynapter(RPackage):
    """Label-free data analysis pipeline for optimal identification and quantitation

    The synapter package provides functionality to reanalyse label-free proteomics data acquired on a Synapt G2 mass spectrometer. One or several runs, possibly processed with additional ion mobility separation to increase identification accuracy can be combined to other quantitation files to maximise identification and quantitation accuracy.
    """

    homepage = "https://lgatto.github.io/synapter/"
    bioc = "synapter"

    version("2.32.0", commit="0048d2da7a8daa66dca54cb03f51a0e9361ee8ab")
    version("2.26.0", commit="3c6c08401803209eba8de2fe1af391d7568e9eba")

    depends_on("r@3.1:", type=("build", "run"))
    depends_on("r-msnbase@2.1.2:", type=("build", "run"))
    depends_on("r-rcolorbrewer", type=("build", "run"))
    depends_on("r-lattice", type=("build", "run"))
    depends_on("r-qvalue", type=("build", "run"))
    depends_on("r-multtest", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-biostrings", type=("build", "run"))
    depends_on("r-cleaver@1.3.3:", type=("build", "run"))
    depends_on("r-readr@0.2:", type=("build", "run"))
    depends_on("r-rmarkdown@1:", type=("build", "run"))
