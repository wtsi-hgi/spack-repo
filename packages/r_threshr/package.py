# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RThreshr(RPackage):
	"""Threshold Selection and Uncertainty for Extreme Value Analysis

	Provides functions for the selection of thresholds for use in 
    extreme value models, based mainly on the methodology in 
    Northrop, Attalides and Jonathan (2017) <doi:10.1111/rssc.12159>.
    It also performs predictive inferences about future extreme values, 
    based either on a single threshold or on a weighted average of inferences 
    from multiple thresholds, using the 'revdbayes' package 
    <https://cran.r-project.org/package=revdbayes>.   
    At the moment only the case where the data can be treated as 
    independent identically distributed observations is considered.
	"""
	
	homepage = "https://paulnorthrop.github.io/threshr/"
	cran = "threshr" 

	version("1.0.5", md5="b952334a2dd651d614339f36f5087c8d")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-revdbayes@1.3.4:", type=("build", "run"))
	depends_on("r-rust@1.2.2:", type=("build", "run"))
