# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAutoPca(RPackage):
	"""Automatic Variable Reduction Using Principal Component Analysis

	PCA done by eigenvalue decomposition of a data correlation matrix, here it automatically determines the number of factors by eigenvalue greater than 1 and it gives the uncorrelated variables based on the rotated component scores, Such that in each principal component variable which has the high variance are selected. It will be useful for non-statisticians in selection of variables. For more information, see the <http://www.ijcem.org/papers032013/ijcem_032013_06.pdf> web page.
	"""
	
	cran = "auto.pca" 

	version("0.3", md5="3ba02fd178da6e227c05b9cda6a7cbe2")

	depends_on("r-psych", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
