# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiodist(RPackage):
    """Different distance measures

    A collection of software tools for calculating distance measures.
    """

    bioc = "bioDist"

    version("1.80.0", commit="6c5ab76031a4769fee5cb2a57839b6b1f8f8f486")
    version("1.74.0", commit="89a00b0c9395d1dcc742a2db17cc7696d540cd18")

    depends_on("r@2:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-kernsmooth", type=("build", "run"))
