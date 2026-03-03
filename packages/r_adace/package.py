# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdace(RPackage):
	"""Estimator of the Adherer Average Causal Effect

	Estimate the causal treatment effect for subjects that can adhere 
    to one or both of the treatments. Given longitudinal data with missing 
    observations, consistent causal effects are calculated. Unobserved potential
    outcomes are estimated through direct integration as described in: 
    Qu et al., (2019) <doi:10.1080/19466315.2019.1700157> and 
    Zhang et. al., (2021) <doi:10.1080/19466315.2021.1891965>. 
	"""
	
	cran = "adace" 

	version("1.0.2", md5="338325f1f92978dc2e65e9a74200dad5")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
