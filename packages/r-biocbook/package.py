# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiocbook(RPackage):
    """Write, containerize, publish and version Quarto books with Bioconductor

    A BiocBook can be created by authors (e.g. R developers, but also scientists, teachers, communicators, ...) who wish to 1) write (compile a body of biological and/or bioinformatics knowledge), 2) containerize (provide Docker images to reproduce the examples illustrated in the compendium), 3) publish (deploy an online book to disseminate the compendium), and 4) version (automatically generate specific online book versions and Docker images for specific Bioconductor releases).
    """

    homepage = "https://bioconductor.org/packages/BiocBook"
    bioc = "BiocBook"

    version("1.6.0", commit="aefaa072529177a9709dfdde356648fcce8b8145")
    version("1.0.0", commit="4b76fd2c6d03837d4f75614ac36062aa937a202a")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-available", type=("build", "run"))
    depends_on("r-cli", type=("build", "run"))
    depends_on("r-glue", type=("build", "run"))
    depends_on("r-gert", type=("build", "run"))
    depends_on("r-gh", type=("build", "run"))
    depends_on("r-gitcreds", type=("build", "run"))
    depends_on("r-httr", type=("build", "run"))
    depends_on("r-usethis", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-purrr", type=("build", "run"))
    depends_on("r-tibble", type=("build", "run"))
    depends_on("r-rprojroot", type=("build", "run"))
    depends_on("r-stringr", type=("build", "run"))
    depends_on("r-yaml", type=("build", "run"))
    depends_on("r-rlang", type=("build", "run"))
    depends_on("r-quarto", type=("build", "run"))
    depends_on("r-renv", type=("build", "run"))
