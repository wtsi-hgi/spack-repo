# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFbfsearch(RPackage):
	"""Algorithm for Searching the Space of Gaussian Directed Acyclic
Graph Models Through Moment Fractional Bayes Factors

	We propose an objective Bayesian algorithm for searching the space of Gaussian directed acyclic graph (DAG) models. The algorithm proposed makes use of moment fractional Bayes factors (MFBF) and thus it is suitable for learning sparse graph. The algorithm is implemented by using Armadillo: an open-source C++ linear algebra library. 
	"""
	
	cran = "FBFsearch" 

	version("1.2", md5="ef6a65f8bd10bf682e3fb0c8db192541")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
