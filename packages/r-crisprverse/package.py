# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrisprverse(RPackage):
    """Easily install and load the crisprVerse ecosystem for CRISPR gRNA design

    The crisprVerse is a modular ecosystem of R packages developed for the design and manipulation of CRISPR guide RNAs (gRNAs). All packages share a common language and design principles. This package is designed to make it easy to install and load the crisprVerse packages in a single step. To learn more about the crisprVerse, visit <https://www.github.com/crisprVerse>.
    """

    homepage = "https://github.com/crisprVerse/crisprVerse"
    bioc = "crisprVerse"

    version("1.10.0", commit="3ed7c9e79908ffe383ebf6c462dcc107301c2224")
    version("1.4.0", commit="8cad1eac5b6755c90d7b8eebd78e6d2a5e00f4af")

    depends_on("r@4.2:", type=("build", "run"))
    depends_on("r-biocmanager", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-crisprbase", type=("build", "run"))
    depends_on("r-crisprbowtie", type=("build", "run"))
    depends_on("r-crisprscore", type=("build", "run"))
    depends_on("r-crisprscoredata", type=("build", "run"))
    depends_on("r-crisprdesign", type=("build", "run"))
    depends_on("r-crisprviz", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
