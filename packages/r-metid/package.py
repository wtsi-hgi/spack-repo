# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetid(RPackage):
    """Network-based prioritization of putative metabolite IDs

    This package uses an innovative network-based approach that will enhance our ability to determine the identities of significant ions detected by LC-MS.
    """

    homepage = "https://github.com/ressomlab/MetID"
    bioc = "MetID"

    version("1.26.0", commit="e40e84e6e4e5e9d0ce827ca42e50b1224e196d87")
    version("1.20.0", commit="635ed59e2c3aaa3b2d510b45ad954b670a078477")

    depends_on("r@3.5:", type=("build", "run"))
    depends_on("r-devtools@1.13:", type=("build", "run"))
    depends_on("r-stringr@1.3:", type=("build", "run"))
    depends_on("r-matrix@1.2.12:", type=("build", "run"))
    depends_on("r-igraph@1.2.1:", type=("build", "run"))
    depends_on("r-chemminer@2.30.2:", type=("build", "run"))
