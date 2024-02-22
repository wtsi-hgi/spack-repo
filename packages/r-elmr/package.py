# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RElmr(RPackage):
	"""Extreme Machine Learning (ELM)

	Training and prediction functions are provided for the Extreme Learning Machine algorithm (ELM). The ELM use a Single Hidden Layer Feedforward Neural Network (SLFN) with random generated weights and no gradient-based backpropagation. The training time is very short and the online version allows to update the model using small chunk of the training set at each iteration. The only parameter to tune is the hidden layer size and the learning function.
	"""
	
	cran = "ELMR" 

	version("1.0", md5="e8fdcdae1c1b464cd134dbdfe04723b4")

	depends_on("r@3.2.2:", type=("build", "run"))
