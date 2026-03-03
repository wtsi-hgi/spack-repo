# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBild(RPackage):
	"""A Package for BInary Longitudinal Data

	Performs logistic regression for binary longitudinal
  data, allowing for serial dependence among observations from a given
  individual and a random intercept term. Estimation is via maximization
  of the exact likelihood of a suitably defined model. Missing values and 
  unbalanced data are allowed, with some restrictions. 
  M. Helena Goncalves et al.(2007) <DOI: 10.18637/jss.v046.i09>.
	"""
	
	cran = "bild" 

	version("1.2-1", md5="c6b7ccfe377b58daf267919062e1ff10")

	depends_on("r@3.1:", type=("build", "run"))
