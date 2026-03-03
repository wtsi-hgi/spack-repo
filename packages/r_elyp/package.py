# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElyp(RPackage):
	"""Empirical Likelihood Analysis for the Cox Model and
Yang-Prentice (2005) Model

	Empirical likelihood ratio tests for the Yang and Prentice (short/long term hazards ratio) models. 
             Empirical likelihood tests within a Cox model, for parameters defined via 
			 both baseline hazard function and regression parameters.
	"""
	
	homepage = "http://www.ms.uky.edu/~mai/EmpLik.html"
	cran = "ELYP" 

	version("0.7-5", md5="043fcb53b9646cd0cbcac69c0a62f8a2")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
