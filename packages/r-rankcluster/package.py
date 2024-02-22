# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRankcluster(RPackage):
	"""Model-Based Clustering for Multivariate Partial Ranking Data

	Implementation of a model-based clustering algorithm for
    ranking data (C. Biernacki, J. Jacques (2013) <doi:10.1016/j.csda.2012.08.008>). 
    Multivariate rankings as well as partial rankings are taken
    into account. This algorithm is based on an extension of the Insertion
    Sorting Rank (ISR) model for ranking data, which is a meaningful and
    effective model parametrized by a position parameter (the modal ranking,
    quoted by mu) and a dispersion parameter (quoted by pi). The heterogeneity
    of the rank population is modelled by a mixture of ISR, whereas conditional
    independence assumption is considered for multivariate rankings.
	"""
	
	cran = "Rankcluster" 

	version("0.98.0", md5="167f9954d9673db453e3c756d5400c9c")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
