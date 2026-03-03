# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobustmeta(RPackage):
	"""Robust Inference for Meta-Analysis with Influential Outlying
Studies

	Robust inference methods for fixed-effect and random-effects models of meta-analysis are implementable. The robust methods are developed using the density power divergence that is a robust estimating criterion developed in machine learning theory, and can effectively circumvent biases and misleading results caused by influential outliers. The density power divergence is originally introduced by Basu et al. (1998) <doi:10.1093/biomet/85.3.549>, and the meta-analysis methods are developed by Noma et al. (2022) <forthcoming>.
	"""
	
	cran = "robustmeta" 

	version("1.2-1", md5="7d75c08c6e7265e1502c2599b0ce3039")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
