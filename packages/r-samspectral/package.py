# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamspectral(RPackage):
    """Identifies cell population in flow cytometry data

    Samples large data such that spectral clustering is possible while preserving density information in edge weights. More specifically, given a matrix of coordinates as input, SamSPECTRAL first builds the communities to sample the data points. Then, it builds a graph and after weighting the edges by conductance computation, the graph is passed to a classic spectral clustering algorithm to find the spectral clusters. The last stage of SamSPECTRAL is to combine the spectral clusters. The resulting "connected components" estimate biological cell populations in the data. See the vignette for more details on how to use this package, some illustrations, and simple examples.
    """

    bioc = "SamSPECTRAL"

    version("1.62.0", commit="e3f3031f4f5384c2e6229f6caf2043163c874963")
    version("1.56.0", commit="a7b13c3bbd51fd50e771857651f5bae783eb7326")

    depends_on("r@3.3.3:", type=("build", "run"))
