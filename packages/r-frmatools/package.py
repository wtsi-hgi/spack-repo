# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFrmatools(RPackage):
    """Frozen RMA Tools

    Tools for advanced use of the frma package.
    """

    homepage = "http://bioconductor.org"
    bioc = "frmaTools"

    version("1.60.0", commit="dee6348c28d5bfd9a81764ce71614c2710ac25b4")
    version("1.54.0", commit="ef06a14c7f5454256f4f5b23fb1c37888045d2d8")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-affy", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-dbi", type=("build", "run"))
    depends_on("r-preprocesscore", type=("build", "run"))
