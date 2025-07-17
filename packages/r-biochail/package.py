# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiochail(RPackage):
    """basilisk and hail

    Use hail via basilisk when appropriate, or via reticulate. This package can be used in terra.bio to interact with UK Biobank resources processed by hail.is.
    """

    homepage = "https://github.com/vjcitn/BiocHail"
    bioc = "BiocHail"

    version("1.8.0", commit="747e24e4b71d2ae81c955941aa4e2b946acca96b")
    version("1.2.0", commit="791b18075325cc220d11070277b2290e1f9dcd54")

    depends_on("r@4.3:", type=("build", "run"))
    depends_on("r-reticulate", type=("build", "run"))
    depends_on("r-basilisk", type=("build", "run"))
    depends_on("r-biocfilecache", type=("build", "run"))
    depends_on("r-dplyr", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
