# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCghbase(RPackage):
    """CGHbase: Base functions and classes for arrayCGH data analysis.

    Contains functions and classes that are needed by arrayCGH packages.
    """

    homepage = "https://github.com/tgac-vumc/CGHbase"
    bioc = "CGHbase"

    version("1.68.0", commit="ae87494b4cdc16d104ad83bd998d8ae24481ba91")
    version("1.62.0", commit="536388705123a3efd35481d70538eb11e6bf8963")

    depends_on("r@2.10:", type=("build", "run"))
    depends_on("r-biobase@2.5.5:", type=("build", "run"))
    depends_on("r-marray", type=("build", "run"))
