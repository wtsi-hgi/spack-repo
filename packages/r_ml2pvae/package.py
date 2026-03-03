# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMl2pvae(RPackage):
	"""Variational Autoencoder Models for IRT Parameter Estimation

	Based on the work of Curi, Converse, Hajewski, and Oliveira (2019) <doi:10.1109/IJCNN.2019.8852333>. This package provides easy-to-use functions which create a variational autoencoder (VAE) to be used for parameter estimation in Item Response Theory (IRT) - namely the Multidimensional Logistic 2-Parameter (ML2P) model. To use a neural network as such, nontrivial modifications to the architecture must be made, such as restricting the nonzero weights in the decoder according to some binary matrix Q. The functions in this package allow for straight-forward construction, training, and evaluation so that minimal knowledge of 'tensorflow' or 'keras' is required. 
	"""
	
	homepage = "https://converseg.github.io"
	cran = "ML2Pvae" 

	version("1.0.0.1", md5="50bf6369e0632f8626b0db6c246fa9db")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-keras@2.3:", type=("build", "run"))
	depends_on("r-reticulate@1:", type=("build", "run"))
	depends_on("r-tensorflow@2.2:", type=("build", "run"))
	depends_on("r-tfprobability@0.11:", type=("build", "run"))
	depends_on("py-tensorflow-probability", type=("build", "link", "run"))
