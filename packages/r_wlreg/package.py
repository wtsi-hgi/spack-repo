# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWlreg(RPackage):
	"""Regression Analysis Based on Win Loss Endpoints

	Use various regression models for the analysis of win loss endpoints 
             adjusting for non-binary and multivariate covariates.
	"""
	
	cran = "WLreg" 

	version("1.0.0.1", md5="90a4fa9a95aed123cdae4d9d65b6f631")

	depends_on("r@3.1.2:", type=("build", "run"))
	depends_on("r-inline", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
