# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIterclust(RPackage):
    """Iterative Clustering

    A framework for performing clustering analysis iteratively.
    """

    homepage = "https://github.com/hd2326/iterClust"
    bioc = "iterClust"

    version("1.24.0", commit="a81011d0755baf6a82a9fe7f3392664d007cdce4")

    depends_on("r@3.4.1:", type=("build", "run"))
    depends_on("r-biobase", type=("build", "run"))
    depends_on("r-cluster", type=("build", "run"))
