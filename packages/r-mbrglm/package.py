# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMbrglm(RPackage):
	"""Median Bias Reduction in Binomial-Response GLMs

	Fit generalized linear models with binomial responses using  a median modified score approach (Kenne Pagui et al., 2016, <https://arxiv.org/abs/1604.04768>) to median bias reduction. This method respects equivariance under reparameterizations for each parameter component and also solves the infinite estimates problem (data separation).
	"""
	
	cran = "mbrglm" 

	version("0.0.1", md5="651e7e719c7ae2b92bab3d7889cf1369")

	depends_on("r@2.6:", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-enrichwith", type=("build", "run"))
