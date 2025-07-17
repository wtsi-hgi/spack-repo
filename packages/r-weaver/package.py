# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWeaver(RPackage):
    """Tools and extensions for processing Sweave documents

    This package provides enhancements on the Sweave() function in the base package.  In particular a facility for caching code chunk results is included.
    """

    bioc = "weaver"

    version("1.74.0", commit="6dea8b3bb9574a6319a3e33235cb9679ba539e40")
    version("1.68.0", commit="707e64336ddc7f7d7af0df1550e923bb74bf2770")

    depends_on("r@2.5:", type=("build", "run"))
    depends_on("r-digest", type=("build", "run"))
    depends_on("r-codetools", type=("build", "run"))
