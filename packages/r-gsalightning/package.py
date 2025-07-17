# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsalightning(RPackage):
    """Fast Permutation-based Gene Set Analysis

    GSALightning provides a fast implementation of permutation-based gene set analysis for two-sample problem. This package is particularly useful when testing simultaneously a large number of gene sets, or when a large number of permutations is necessary for more accurate p-values estimation.
    """

    homepage = "https://github.com/billyhw/GSALightning"
    bioc = "GSALightning"

    version("1.36.0", commit="f35992dad54471a3553c7eba653fa846c3c22000")
    version("1.30.0", commit="df599d9071a13cc11ae113086a36b731603502fa")

    depends_on("r@3.3:", type=("build", "run"))
    depends_on("r-matrix", type=("build", "run"))
    depends_on("r-data-table", type=("build", "run"))
