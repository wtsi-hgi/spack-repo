# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArco(RPackage):
	"""Artificial Counterfactual Package

	Set of functions to analyse and estimate Artificial Counterfactual models from Carvalho, Masini and Medeiros (2016) <DOI:10.2139/ssrn.2823687>.
	"""
	
	cran = "ArCo" 

	version("0.3-1", md5="107b35795b33b9dbbee6061fa2b8c775")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
