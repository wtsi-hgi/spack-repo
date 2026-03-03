# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImnn(RPackage):
	"""Neural Networks for Predicting Volume of Forest Trees

	Neural network has potential in forestry modelling. This package is designed to create and assess Artificial Intelligence based Neural Networks with varying architectures for prediction of volume of forest trees using two input features: height and diameter at breast height, as they are the key factors in predicting volume, therefore development and validation of efficient volume prediction neural network model is necessary. This package has been developed using the algorithm of Tabassum et al. (2022) <doi:10.18805/ag.D-5555>.
	"""
	
	cran = "ImNN" 

	version("0.1.0", md5="d41e385f25d75b8cb5641655999a168b")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mlmetrics", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
