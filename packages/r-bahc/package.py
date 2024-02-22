# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBahc(RPackage):
	"""Filter Covariance and Correlation Matrices with
Bootstrapped-Averaged Hierarchical Ansatz

	A method to filter correlation and covariance matrices by averaging
     bootstrapped filtered hierarchical clustering and boosting. See Ch. Bongiorno and D. Challet,
     Covariance matrix filtering with bootstrapped hierarchies (2020) <arXiv:2003.05807> and
     Ch. Bongiorno and D. Challet, Reactive Global Minimum Variance Portfolios with k-BAHC covariance cleaning
     (2020) <arXiv:2005.08703>.
	"""
	
	cran = "bahc" 

	version("0.3.0", md5="3aa29ca4c8a32b323fedf9e5fa5cab70")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
