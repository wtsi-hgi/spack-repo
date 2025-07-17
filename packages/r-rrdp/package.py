# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRrdp(RPackage):
    """Interface to the RDP Classifier

    Seamlessly interfaces RDP classifier (version 2.9).
    """

    bioc = "rRDP"

    version("1.42.0", commit="d6635ee1bf1892588f90c15c778abbfa6e0bee3d")
    version("1.36.0", commit="b269f9e2e286d76aee8a89c0d72a5cea40671f67")

    depends_on("r-biostrings@2.26.2:", type=("build", "run"))
    depends_on("openjdk@1.4:", type=("build", "link", "run"))
