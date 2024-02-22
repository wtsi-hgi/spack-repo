# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RUltimixt(RPackage):
	"""Bayesian Analysis of Location-Scale Mixture Models using a
Weakly Informative Prior

	A generic reference Bayesian analysis of unidimensional mixture distributions obtained by a location-scale parameterisation of the model is implemented. The including functions simulate and summarize posterior samples for location-scale mixture models using a weakly informative prior. There is no need to define priors for scale-location parameters except two hyperparameters in which are associated with a Dirichlet prior for weights and a simplex.
	"""
	
	cran = "Ultimixt" 

	version("2.1", md5="0bd72b56d77d1852fbf0fd97ced9dd35")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
