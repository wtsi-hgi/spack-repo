# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAnn2(RPackage):
	"""Artificial Neural Networks for Anomaly Detection

	Training of neural networks for classification and regression tasks
	using mini-batch gradient descent. Special features include a function for 
	training autoencoders, which can be used to detect anomalies, and some 
	related plotting functions. Multiple activation functions are supported, 
	including tanh, relu, step and ramp. For the use of the step and ramp 
	activation functions in detecting anomalies using autoencoders, see 
	Hawkins et al. (2002) <doi:10.1007/3-540-46145-0_17>. Furthermore, 
	several loss functions are supported, including robust ones such as Huber 
	and pseudo-Huber loss, as well as L1 and L2 regularization. The possible 
	options for optimization algorithms are RMSprop, Adam and SGD with momentum.
	The package contains a vectorized C++ implementation that facilitates 
	fast training through mini-batch learning.
	"""
	
	homepage = "https://github.com/bflammers/ANN2"
	cran = "ANN2"

	version("2.3.4", md5="b3b411b1cf0d8dfb35e657e39fba37ca", url="https://cran.r-project.org/src/contrib/ANN2_2.3.4.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-reshape2@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@3:", type=("build", "run"))
	depends_on("r-viridislite@0.3:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
