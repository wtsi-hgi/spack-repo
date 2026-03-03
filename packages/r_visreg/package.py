# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVisreg(RPackage):
	"""Visualization of Regression Models

	Provides a convenient interface for constructing plots to visualize the fit of regression models arising from a wide variety of models in R ('lm', 'glm', 'coxph', 'rlm', 'gam', 'locfit', 'lmer', 'randomForest', etc.)
	"""
	
	homepage = "http://pbreheny.github.io/visreg"
	cran = "visreg" 

	version("2.7.0", md5="a3ceeccc63e4a9391a2edfd156d8d786")

	depends_on("r-lattice", type=("build", "run"))
