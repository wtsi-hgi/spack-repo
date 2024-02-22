# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgmr(RPackage):
	"""Generalized Gauss Markov Regression

	Implements the generalized Gauss Markov regression, this is useful when both predictor and response have uncertainty attached to them and also when covariance within the predictor, within the response and between the predictor and the response is present. Base on the results published in guide ISO/TS 28037 (2010) <https://www.iso.org/standard/44473.html>. 
	"""
	
	cran = "ggmr" 

	version("0.1.1", md5="fff5323090dcd46f1e952f959fd06456")

	depends_on("r-mass@7.3:", type=("build", "run"))
	depends_on("r@3.4:", type=("build", "run"))
