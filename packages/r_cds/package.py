# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCds(RPackage):
	"""Constrained Dual Scaling for Detecting Response Styles

	This is an implementation of constrained dual scaling for
    detecting response styles in categorical data, including utility functions. The
    procedure involves adding additional columns to the data matrix representing the
    boundaries between the rating categories. The resulting matrix is then doubled
    and analyzed by dual scaling. One-dimensional solutions are sought which provide
    optimal scores for the rating categories. These optimal scores are constrained
    to follow monotone quadratic splines. Clusters are introduced within which the
    response styles can vary. The type of response style present in a cluster can
    be diagnosed from the optimal scores for said cluster, and this can be used to
    construct an imputed version of the data set which adjusts for response styles.
	"""
	
	cran = "cds" 

	version("1.0.3", md5="e1ce86dd4a0e9112a0f596062ab6562f")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
	depends_on("r-clue", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-copula", type=("build", "run"))
