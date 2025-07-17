# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNcigraphdata(RPackage):
    """Data for the NCIgraph software package

    Provides pathways from the NCI Pathways Database as R graph objects
    """

    bioc = "NCIgraphData"

    version("1.44.0", commit="38557fbcb0f53408a7b1ae589c93490498f7a4b7")
    version("1.38.0", commit="b84956a7ad2b981254273256a82864a8c1cbb74d")

    depends_on("r@2.10:", type=("build", "run"))
