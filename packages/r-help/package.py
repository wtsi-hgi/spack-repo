# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHelp(RPackage):
    """Tools for HELP data analysis

    The package contains a modular pipeline for analysis of HELP microarray data, and includes graphical and mathematical tools with more general applications.
    """

    bioc = "HELP"

    version("1.66.0", commit="5578865648ba093910aa2949a9e1cba78f25d059")
    version("1.60.0", commit="26db6a6564825650c0461cbb240bbe7da4e5e48b")

    depends_on("r@2.8:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
