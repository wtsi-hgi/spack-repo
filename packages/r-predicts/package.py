# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredicts(RPackage):
	"""Spatial Prediction Tools

	Methods for spatial predictive modeling, especially for spatial distribution models. This includes algorithms for model fitting and prediction, as well as methods for model evaluation. 
	"""
	
	homepage = "https://rspatial.org/sdm/"
	cran = "predicts" 

	version("0.1-11", md5="df7da4ba47e243fa8a7b6ddd0d1005ae")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
