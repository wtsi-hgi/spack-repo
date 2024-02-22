# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDissmod(RPackage):
	"""Fitting Sample Selection Models for Discrete Response Variables

	Tools to fit sample selection models in case of discrete response 
  variables, through a parametric formulation which represents a natural 
  extension of the well-known Heckman selection model are provided in the 
  package. The response variable can be of Bernoulli, Poisson or Negative 
  Binomial type. The sample selection mechanism allows to choose among a 
  Normal, Logistic or Gumbel distribution.
	"""
	
	cran = "DiSSMod" 

	version("1.0.0", md5="c4d1a3f8f3b8b3392f2e089166880f23")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
	depends_on("r-matrixcalc", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
