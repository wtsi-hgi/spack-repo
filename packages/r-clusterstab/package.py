# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RClusterstab(RPackage):
    """Compute cluster stability scores for microarray data

    This package can be used to estimate the number of clusters in a set of microarray data, as well as test the stability of these clusters.
    """

    bioc = "clusterStab"

    version("1.80.0", commit="02b8d48882fb6892fedcc89ebf597f0524f2fe8d")
    version("1.74.0", commit="6bbc33b67f359ba1c2bc686d29b7152ccb7cd8a4")

    depends_on("r-biobase@1.4.22:", type=("build", "run"))
    depends_on("r@1.9:", type=("build", "run"))
