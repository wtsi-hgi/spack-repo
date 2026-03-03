# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCtqr(RPackage):
	"""Censored and Truncated Quantile Regression

	Estimation of quantile regression models for survival data.
	"""
	
	cran = "ctqr" 

	version("2.1", md5="4729d0c88ee1815c4a951475d5a5db5a")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-pch@2.1:", type=("build", "run"))
