# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmpath(RPackage):
	"""L1 Regularization Path for Generalized Linear Models and Cox
Proportional Hazards Model

	A path-following algorithm for L1 regularized generalized linear models and Cox proportional hazards model.
	"""
	
	cran = "glmpath" 

	version("0.98", md5="b3bdf595170f157c0c9065ebf9e79427")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r@2:", type=("build", "run"))
