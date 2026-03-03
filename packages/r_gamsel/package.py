# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGamsel(RPackage):
	"""Fit Regularization Path for Generalized Additive Models

	Using overlap grouped-lasso penalties, 'gamsel' selects whether a term in a 'gam' is nonzero, linear, or a non-linear spline (up to a specified max df per variable). It fits the entire regularization path on a grid of values for the overall penalty lambda, both for gaussian and binomial families.
	"""
	
	homepage = "https://arxiv.org/abs/1506.03850"
	cran = "gamsel" 

	version("1.8-2", md5="790106ff940a49470458d9b4259fad61")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
