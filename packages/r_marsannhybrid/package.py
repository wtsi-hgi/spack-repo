# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMarsannhybrid(RPackage):
	"""MARS Based ANN Hybrid Model

	Multivariate Adaptive Regression Spline (MARS) based Artificial Neural Network (ANN) hybrid model is combined Machine learning hybrid approach which selects important variables using MARS and then fits ANN on the extracted important variables.
	"""
	
	cran = "MARSANNhybrid" 

	version("0.1.0", md5="c7888c12aee9028dcabc658b51d674f2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
