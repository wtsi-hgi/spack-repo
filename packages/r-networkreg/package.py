# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNetworkreg(RPackage):
	"""Regression Model on Network-Linked Data with Statistical
Inference

	Linear regression model with nonparametric network effects on network-linked observations. The model is proposed by Le and Li (2022) <arXiv:2007.00803> and is assumed on observations that are connected by a network or similar relational data structure. The model does not assume that the relational data or network structure to be precisely observed; thus, the method is provably robust to a certain level of perturbation of the network structure. The package contains the estimation and inference function for the model.
	"""
	
	cran = "NetworkReg" 

	version("1.1", md5="419c5a6c8963cb9121651b5e4cb3ed7e")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-randnet", type=("build", "run"))
	depends_on("r-rspectra", type=("build", "run"))
