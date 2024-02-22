# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrq(RPackage):
	"""Bayesian Analysis of Quantile Regression Models

	Bayesian estimation and variable selection for quantile regression models.
	"""
	
	cran = "Brq" 

	version("3.0", md5="9fc79668a2566635ff4c91d5a79eaef2")

