# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSelex(RPackage):
    """Functions for analyzing SELEX-seq data

    Tools for quantifying DNA binding specificities based on SELEX-seq data.
    """

    homepage = "https://bussemakerlab.org/site/software/"
    bioc = "SELEX"

    version("1.40.0", commit="2536d7bf1bc3b13f654aa7382aa4108e3eb8da90")
    version("1.34.0", commit="bbfab0a8aba1480e4ac68511d844079659c7d5ad")

    depends_on("r-rjava@0.5.0:", type=("build", "run"))
    depends_on("r-biostrings@2.26:", type=("build", "run"))
    depends_on("openjdk@1.5:", type=("build", "link", "run"))
