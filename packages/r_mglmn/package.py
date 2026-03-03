# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMglmn(RPackage):
	"""Model Averaging for Multivariate GLM with Null Models

	Tools for univariate and multivariate generalized linear models with model averaging and null model technique.
	"""
	
	homepage = "https://github.com/mattocci27/mglmn"
	cran = "mglmn" 

	version("0.1.0", md5="127dbc684fc064a513a7f49878dc7d1c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mvabund", type=("build", "run"))
	depends_on("r-snowfall", type=("build", "run"))
