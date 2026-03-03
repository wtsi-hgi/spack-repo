# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMultilcirt(RPackage):
	"""Multidimensional Latent Class Item Response Theory Models

	Framework for the Item Response Theory analysis of dichotomous and ordinal polytomous outcomes under the assumption of multidimensionality and discreteness of the latent traits. The fitting algorithms allow for missing responses and for different item parameterizations and are based on the Expectation-Maximization paradigm. Individual covariates affecting the class weights may be included in the new version (since 2.1).
	"""
	
	cran = "MultiLCIRT" 

	version("2.11", md5="e08880225b45e94d3472aaade20d84eb")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-limsolve", type=("build", "run"))
