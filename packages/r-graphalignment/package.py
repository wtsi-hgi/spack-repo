# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGraphalignment(RPackage):
    """GraphAlignment

    Graph alignment is an extension package for the R programming environment which provides functions for finding an alignment between two networks based on link and node similarity scores. (J. Berg and M. Laessig, "Cross-species analysis of biological networks by Bayesian alignment", PNAS 103 (29), 10967-10972 (2006))
    """

    homepage = "http://www.thp.uni-koeln.de/~berg/GraphAlignment/"
    bioc = "GraphAlignment"

    version("1.72.0", commit="04a86774d47dc6bb7561cd417466e8ed212611cb")
    version("1.66.0", commit="913ea0cfab9dfd08ff27fa6fb36c604bb4cbebd7")
