# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSurvml(RPackage):
	"""Flexible Estimation of Conditional Survival Functions Using
Machine Learning

	Tools for flexible estimation of conditional survival 
              functions using off-the-shelf machine learning tools. Implements both 
              global and local survival stacking. See Wolock CJ, Gilbert PB,
              Simon N, and Carone M (2022+) <arXiv:2211.03031>. 
	"""
	
	homepage = "https://github.com/cwolock/survML"
	cran = "survML" 

	version("1.0.0", md5="311c00c7cce6de6aee213180316cbe37")

	depends_on("r-superlearner@2.0.28:", type=("build", "run"))
	depends_on("r-iso@0.0.18.1:", type=("build", "run"))
