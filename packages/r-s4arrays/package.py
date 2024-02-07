# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RS4arrays(RPackage):
    """The S4Arrays package defines the Array virtual class to be extended by other S4 classes that wish to implement a container with an array-like semantic."""

    homepage = "https://github.com/Bioconductor/S4Arrays"

    #git = "https://github.com/Bioconductor/S4Arrays"
    #version("1.3.3", commit="34fadf9")

    bioc = "S4Arrays"
    urls = "https://bioconductor.org/packages/release/bioc/src/contrib/S4Arrays_1.2.0.tar.gz"

    version("1.2.0", md5="c77474b839251d19d31708831de3c1bf")

    depends_on("r@4.3.0:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-abind", type=("build", "run"))
    depends_on("r-biocgenerics", type=("build", "run"))
    depends_on("r-s4vectors", type=("build", "run"))
    depends_on("r-iranges", type=("build", "run"))
    depends_on("r-crayon", type=("build", "run"))
 
