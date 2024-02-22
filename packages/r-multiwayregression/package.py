# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultiwayregression(RPackage):
	"""Perform Tensor-on-Tensor Regression

	Functions to predict one multi-way array (i.e., a tensor) from another multi-way array, using a low-rank CANDECOMP/PARAFAC (CP) factorization and a ridge (L_2) penalty [Lock, EF (2018) <doi:10.1080/10618600.2017.1401544>].  Also includes functions to sample from the Bayesian posterior of a tensor-on-tensor model.      
	"""
	
	cran = "MultiwayRegression" 

	version("1.2", md5="2fd6fedfdb7ed2ba5e541127e3858570")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
