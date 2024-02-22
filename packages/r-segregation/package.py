# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSegregation(RPackage):
	"""Entropy-Based Segregation Indices

	Computes segregation indices, including the Index of Dissimilarity,
    as well as the information-theoretic indices developed by
    Theil (1971) <isbn:978-0471858454>, namely
    the Mutual Information Index (M) and Theil's Information Index (H).
    The M, further described by Mora and Ruiz-Castillo (2011) <doi:10.1111/j.1467-9531.2011.01237.x>
    and Frankel and Volij (2011) <doi:10.1016/j.jet.2010.10.008>,
    is a measure of segregation that is highly decomposable. The package provides
    tools to decompose the index by units and groups (local segregation),
    and by within and between terms. The package also provides a method to decompose
    differences in segregation as described by Elbers (2021) <doi:10.1177/0049124121986204>.
    The package includes standard error estimation by bootstrapping, which also corrects for
    small sample bias. The package also contains functions for visualizing segregation patterns.
	"""
	
	homepage = "https://elbersb.github.io/segregation/"
	cran = "segregation" 

	version("1.1.0", md5="1d4516b2b6cb28b97d2f91e9cf108471")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
