# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBridgedbr(RPackage):
    """Code for using BridgeDb identifier mapping framework from within R

    Use BridgeDb functions and load identifier mapping databases in R. It uses GitHub, Zenodo, and Figshare if you use this package to download identifier mappings files.
    """

    homepage = "https://github.com/bridgedb/BridgeDbR"
    bioc = "BridgeDbR"

    version("2.18.0", commit="f0a2e0cd46f720e4d51e5ff0350b732fc414928a")
    version("2.12.0", commit="b2989b33298bff24acc8c309218c7e7f630b1fc4")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-rjava", type=("build", "run"))
    depends_on("r-curl", type=("build", "run"))
