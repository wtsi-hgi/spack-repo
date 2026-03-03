# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeepnet(RPackage):
	"""Deep Learning Toolkit in R

	Implement some deep learning architectures and neural network
    algorithms, including BP,RBM,DBN,Deep autoencoder and so on.
	"""
	
	cran = "deepnet" 

	version("0.2.1", md5="90b4237b2c26263d21fd617f3ed73ed1")

