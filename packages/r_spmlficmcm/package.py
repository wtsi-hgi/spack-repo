# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpmlficmcm(RPackage):
	"""Semiparametric Maximum Likelihood Method for Interactions
Gene-Environment in Case-Mother Control-Mother Designs

	Implements the method of general semiparametric maximum likelihood estimation for logistic models in case-mother control-mother designs.
	"""
	
	cran = "SPmlficmcm" 

	version("1.4", md5="952770efb6e70924e8ff3ae15798adae")

	depends_on("r-nleqslv", type=("build", "run"))
