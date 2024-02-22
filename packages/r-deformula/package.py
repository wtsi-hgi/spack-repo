# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeformula(RPackage):
	"""Integration of One-Dimensional Functions with Double Exponential
Formulas

	Numerical quadrature of functions of one variable over a finite
  or infinite interval with double exponential formulas.
	"""
	
	homepage = "https://github.com/okamumu/deformula/"
	cran = "deformula" 

	version("0.1.2", md5="4302e9bda10ade7c65db609ca95a0f99")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-cpp11", type=("build", "run"))
