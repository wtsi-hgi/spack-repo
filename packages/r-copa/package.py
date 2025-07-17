# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopa(RPackage):
    """Functions to perform cancer outlier profile analysis.

    COPA is a method to find genes that undergo recurrent fusion in a given cancer type by finding pairs of genes that have mutually exclusive outlier profiles.
    """

    bioc = "copa"

    version("1.76.0", commit="4987a2e43a2df03e05182d5db4ac25b2133d5e8a")
    version("1.70.0", commit="03fcd667a61f793d8a8cc91bbdb37cf30bf7ba6f")

    depends_on("r-biobase", type=("build", "run"))
