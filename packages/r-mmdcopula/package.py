# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmdcopula(RPackage):
	"""Robust Estimation of Copulas by Maximum Mean Discrepancy

	Provides functions for the robust estimation of 
	parametric families of copulas using minimization of 
	the Maximum Mean Discrepancy, following the article
	Alquier, Chérief-Abdellatif, Derumigny and Fermanian (2022)
	<doi:10.1080/01621459.2021.2024836>.
	"""
	
	cran = "MMDCopula" 

	version("0.2.1", md5="445709edbc83d257ea0a68a8f53a83d1")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-vinecopula", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-randtoolbox", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-wdm", type=("build", "run"))
