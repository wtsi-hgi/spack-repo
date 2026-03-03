# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPredictme(RPackage):
	"""Visualize Individual Prediction Performance

	Enables researchers to visualize the prediction performance of any algorithm on the individual level (or close to it), given that the predicted outcome is either binary or continuous. Visual results are instantly comprehensible.
	"""
	
	homepage = "https://github.com/mmiche/predictMe"
	cran = "predictMe" 

	version("0.1", md5="7836b98e02ae30bfeb34b89b1deedcff")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
