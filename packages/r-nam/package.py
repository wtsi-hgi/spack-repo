# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNam(RPackage):
	"""Nested Association Mapping

	Designed for association studies in nested association mapping (NAM) panels, experimental and random panels. The method is described by Xavier et al. (2015) <doi:10.1093/bioinformatics/btv448>. It includes tools for genome-wide associations of multiple populations, marker quality control, population genetics analysis, genome-wide prediction, solving mixed models and finding variance components through likelihood and Bayesian methods.
	"""
	
	cran = "NAM" 

	version("1.7.3", md5="075192330ef555ee19e40538eb839de0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
