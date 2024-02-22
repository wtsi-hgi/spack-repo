# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmlep(RPackage):
	"""Fit GLM with LEP-Based Penalized Maximum Likelihood

	Efficient algorithms for fitting regularization paths for
        linear or logistic regression models penalized by LEP.
	"""
	
	cran = "glmlep" 

	version("0.2", md5="cd03ac622cb11e90bddec88987ab8c5b")

