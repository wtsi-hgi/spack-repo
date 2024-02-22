# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGlmnetutils(RPackage):
	"""Utilities for 'Glmnet'

	Provides a formula interface for the 'glmnet' package for
    elasticnet regression, a method for cross-validating the alpha parameter,
    and other quality-of-life tools.
	"""
	
	homepage = "https://github.com/hongooi73/glmnetUtils"
	cran = "glmnetUtils" 

	version("1.1.9", md5="948aa58fbea4c80f8493dd06996513c7")

	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
