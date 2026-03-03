# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPmxcv(RPackage):
	"""Integration-Based Coefficients of Variance

	Estimate coefficient of variance percent (CV%) for any arbitrary distribution, including some built-in estimates for commonly-used transformations in pharmacometrics. Methods are described in various sources, but applied here as summarized in: Prybylski, (2024) <doi:10.1007/s40262-023-01343-2>.
	"""
	
	cran = "pmxcv" 

	version("0.0.1.0", md5="8c237b05eb261470d8ae161bcfb94914")

