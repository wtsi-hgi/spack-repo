# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpikeslab(RPackage):
	"""Prediction and Variable Selection Using Spike and Slab
Regression

	Spike and slab for prediction and variable selection in linear regression models. Uses a generalized elastic net for variable selection.
	"""
	
	homepage = "https://ishwaran.org/"
	cran = "spikeslab" 

	version("1.1.6", md5="6beb139979282fa32609216be7ad9674")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
