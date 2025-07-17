# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnbeadsRn5(RPackage):
    """RnBeads.rn5

    Automatically generated RnBeads annotation package for the assembly rn5.
    """

    bioc = "RnBeads.rn5"

    version("1.40.0", commit="2533d7f953bd771a360b8857fb659fdeec270007")
    version("1.34.0", commit="a7291fe77e510fe82111c556df539aceec51e2f2")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-genomicranges", type=("build", "run"))
