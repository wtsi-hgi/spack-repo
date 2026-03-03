# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPassLme(RPackage):
	"""Power and Sample Size for Linear Mixed Effect Models

	Power and sample size calculation for testing fixed effect coefficients in multilevel linear mixed effect models with one or more than one independent populations. Laird, Nan M. and Ware, James H. (1982) <doi:10.2307/2529876>.
	"""
	
	cran = "pass.lme" 

	version("0.9.0", md5="759f0b0312a578bb224637645e735568")

	depends_on("r@3.2.5:", type=("build", "run"))
