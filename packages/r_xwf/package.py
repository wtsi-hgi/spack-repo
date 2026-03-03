# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXwf(RPackage):
	"""Extrema-Weighted Feature Extraction

	Extrema-weighted feature extraction for varying length functional data. Functional data analysis method that performs dimensionality reduction based on predefined features and allows for quantile weighting. Method implemented as presented in van den Boom et al. (2018) <doi:10.1093/bioinformatics/bty120>.
	"""
	
	cran = "xwf" 

	version("0.2-3", md5="f41284c30287c8ca02bcce03d62065e7")

	depends_on("r-mgcv", type=("build", "run"))
