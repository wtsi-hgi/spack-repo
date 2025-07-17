# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRefplus(RPackage):
    """A function set for the Extrapolation Strategy (RMA+) and Extrapolation Averaging (RMA++) methods.

    The package contains functions for pre-processing Affymetrix data using the RMA+ and the RMA++ methods.
    """

    bioc = "RefPlus"

    version("1.72.0", commit="3882623f00f056bd2ffe0984b6c07543acb155c6")

    depends_on("r@2.8:", type=("build", "run"))
    depends_on("r-biobase@2.1:", type=("build", "run"))
    depends_on("r-affy@1.20:", type=("build", "run"))
    depends_on("r-affyplm@1.18:", type=("build", "run"))
    depends_on("r-preprocesscore@1.4:", type=("build", "run"))
