# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopinf(RPackage):
	"""Assumption-Lean and Data-Adaptive Post-Prediction Inference

	Implementation of assumption-lean and data-adaptive post-prediction inference (POPInf), for valid and efficient statistical inference based on data predicted by machine learning. See Miao, Miao, Wu, Zhao, and Lu (2023) <arXiv:2311.14220>.
	"""
	
	homepage = "https://arxiv.org/abs/2311.14220"
	cran = "POPInf" 

	version("1.0.0", md5="3f5725fb5efdeebc1566487084920373")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
