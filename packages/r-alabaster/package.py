# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabaster(RPackage):
    """Umbrella for the Alabaster Framework

    Umbrella for the alabaster suite, providing a single-line import for all alabaster.* packages. Installing this package ensures that all known alabaster.* packages are also installed, avoiding problems with missing packages when a staging method or loading function is dynamically requested. Obviously, this comes at the cost of needing to install more packages, so advanced users and application developers may prefer to install the required alabaster.* packages individually.
    """

    bioc = "alabaster"

    version("1.8.0", commit="8cae2c99f9b0203b8f55ddd2c45bfc19f640b8da")
    version("1.2.0", commit="aa5a401440415b4d6e2cc74efb27cc13a8876670")

    depends_on("r-alabaster-base", type=("build", "run"))
    depends_on("r-alabaster-matrix", type=("build", "run"))
    depends_on("r-alabaster-ranges", type=("build", "run"))
    depends_on("r-alabaster-se", type=("build", "run"))
    depends_on("r-alabaster-sce", type=("build", "run"))
    depends_on("r-alabaster-spatial", type=("build", "run"))
    depends_on("r-alabaster-string", type=("build", "run"))
    depends_on("r-alabaster-vcf", type=("build", "run"))
    depends_on("r-alabaster-bumpy", type=("build", "run"))
    depends_on("r-alabaster-mae", type=("build", "run"))
