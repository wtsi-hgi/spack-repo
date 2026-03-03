# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCopulainference(RPackage):
	"""Estimation and Goodness-of-Fit of Copula-Based Models with
Arbitrary Distributions

	Estimation and goodness-of-fit functions for copula-based models of bivariate data with arbitrary distributions  (discrete, continuous, mixture of both types). The copula families considered here are the  Gaussian, Student, Clayton, Frank, Gumbel, Joe, Plackett, BB1, BB6, BB7,BB8, together with the following non-central squared copula families in Nasri (2020) <doi:10.1016/j.spl.2020.108704>: ncs-gaussian, ncs-clayton, ncs-gumbel, ncs-frank, ncs-joe, and ncs-plackett. For theoretical details, see, e.g., Nasri and Remillard (2023) <arXiv:2301.13408>. 
	"""
	
	cran = "CopulaInference" 

	version("0.5.0", md5="7b63526d4c349839eabc83eb3772fffe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-rvinecopulib", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
