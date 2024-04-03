# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBamlss(RPackage):
	"""Bayesian Additive Models for Location, Scale, and Shape (and
Beyond)

	Infrastructure for estimating probabilistic distributional regression models in a Bayesian framework.
  The distribution parameters may capture location, scale, shape, etc. and every parameter may depend
  on complex additive terms (fixed, random, smooth, spatial, etc.) similar to a generalized additive model.
  The conceptual and computational framework is introduced in Umlauf, Klein, Zeileis (2019)
  <doi:10.1080/10618600.2017.1407325> and the R package in Umlauf, Klein, Simon, Zeileis (2021)
  <doi:10.18637/jss.v100.i04>.
	"""
	
	homepage = "http://www.bamlss.org/"
	cran = "bamlss" 

	version("1.2-2", md5="3730ed71f5d1c06b53112ad2909fa372")
	version("1.2-3", md5="45e9d59e142198ad052ab39fccdacb04")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-coda", type=("build", "run"))
	depends_on("r-colorspace", type=("build", "run"))
	depends_on("r-distributions3@0.2.1:", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
