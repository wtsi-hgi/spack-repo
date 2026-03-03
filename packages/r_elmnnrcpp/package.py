# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElmnnrcpp(RPackage):
	"""The Extreme Learning Machine Algorithm

	Training and predict functions for Single Hidden-layer Feedforward Neural Networks (SLFN) using the Extreme Learning Machine (ELM) algorithm. The ELM algorithm differs from the traditional gradient-based algorithms for very short training times (it doesn't need any iterative tuning, this makes learning time very fast) and there is no need to set any other parameters like learning rate, momentum, epochs, etc. This is a reimplementation of the 'elmNN' package using 'RcppArmadillo' after the 'elmNN' package was archived. For more information, see "Extreme learning machine: Theory and applications" by Guang-Bin Huang, Qin-Yu Zhu, Chee-Kheong Siew (2006), Elsevier B.V, <doi:10.1016/j.neucom.2005.12.126>.
	"""
	
	homepage = "https://github.com/mlampros/elmNNRcpp"
	cran = "elmNNRcpp" 

	version("1.0.4", md5="06462f9f220908a0dc62978e9f808292")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-kernelknn", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8:", type=("build", "run"))
