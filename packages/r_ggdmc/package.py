# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgdmc(RPackage):
	"""Cognitive Models

	Hierarchical Bayesian models. The package provides tools to fit two response time models, using the population-based Markov Chain Monte Carlo. 
	"""
	
	homepage = "https://github.com/yxlin/ggdmc"
	cran = "ggdmc" 

	version("0.2.6.0", md5="ce91a8fad5c02013756125cf771ce358")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rcpp@0.12.10:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.7.100.3:", type=("build", "run"))
