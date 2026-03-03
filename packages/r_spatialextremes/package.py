# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpatialextremes(RPackage):
	"""Modelling Spatial Extremes

	Tools for the statistical modelling of spatial extremes using max-stable processes, copula or Bayesian hierarchical models. More precisely, this package allows (conditional) simulations from various parametric max-stable models, analysis of the extremal spatial dependence, the fitting of such processes using composite likelihoods or least square (simple max-stable processes only), model checking and selection and prediction. Other approaches (although not completely in agreement with the extreme value theory) are available such as the use of (spatial) copula and Bayesian hierarchical models assuming the so-called conditional assumptions. The latter approaches is handled through an (efficient) Gibbs sampler. Some key references: Davison et al. (2012) <doi:10.1214/11-STS376>, Padoan et al. (2010) <doi:10.1198/jasa.2009.tm08577>, Dombry et al. (2013) <doi:10.1093/biomet/ass067>.
	"""
	
	homepage = "http://spatialextremes.r-forge.r-project.org/"
	cran = "SpatialExtremes" 

	version("2.1-0", md5="d1522cbdfe234d8dd5605bef3d2c18e1")

	depends_on("r@1.8:", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
