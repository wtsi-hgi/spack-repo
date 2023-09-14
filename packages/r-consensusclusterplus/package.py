# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConsensusclusterplus(RPackage):
    """Algorithm for determining cluster count and membership by stability evidence in unsupervised analysis."""

    url = "https://bioconductor.org/packages/release/bioc/src/contrib/ConsensusClusterPlus_1.64.0.tar.gz"
    bioc = "ConsensusClusterPlus"

    version("1.64.0", sha256="b5a9b613cefa1ee26f6a34d3cee65816451e5ed6c8b7dc892cbe82d3a0ebe645")

    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-all", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
    'Biobase', 'ALL', 'cluster'
