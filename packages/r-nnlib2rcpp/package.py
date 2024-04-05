# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNnlib2rcpp(RPackage):
	"""A Tool for Creating Custom Neural Networks in C++ and using Them
in R

	Contains a module to define neural networks from custom components and versions of Autoencoder, BP, LVQ, MAM NN.
	"""
	
	homepage = "https://github.com/VNNikolaidis/nnlib2Rcpp"
	cran = "nnlib2Rcpp" 

	version("0.2.5", md5="ed5c56cb3eb6bd568d832976de0f6d9a")
	version("0.2.4", md5="f499846acae0d61a9f1a0e4c09114634")

	depends_on("r-rcpp", type=("build", "run"))
