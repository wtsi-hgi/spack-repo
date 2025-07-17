# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvert(RPackage):
    """Convert Microarray Data Objects

    Define coerce methods for microarray data objects.
    """

    homepage = "http://bioinf.wehi.edu.au/limma/convert.html"
    bioc = "convert"

    version("1.84.0", commit="801274c62baa5a572619a86ee338b0db54b63c14")
    version("1.78.0", commit="398d7e4cccda0c90d963117cac574032f8874e7c")

    depends_on("r@2.6:", type=("build", "run"))
    depends_on("r-biobase@1.15.33:", type=("build", "run"))
    depends_on("r-limma@1.7:", type=("build", "run"))
    depends_on("r-marray", type=("build", "run"))
