# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmvsd(RPackage):
	"""Variable Selection Deviation Measures and Instability Tests for
High-Dimensional Generalized Linear Models

	Variable selection deviation (VSD) measures and instability tests for high-dimensional model selection methods such as LASSO, SCAD and MCP, etc., to decide whether the sparse patterns identified by those methods are reliable. 
	"""
	
	homepage = "https://github.com/emeryyi/glmvsd"
	cran = "glmvsd" 

	version("1.5", md5="f3b6d070b1cf0a8c04959a015a2288b4")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-ncvreg", type=("build", "run"))
	depends_on("r-brglm", type=("build", "run"))
