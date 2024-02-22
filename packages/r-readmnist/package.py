# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadmnist(RPackage):
	"""Read MNIST Dataset

	You can use the function Read.mnist() to read data and arrange them properly from MNIST dataset (the open handwriting digit database <http://yann.lecun.com/exdb/mnist/>). With this package, you can conveniently get all of necessary informations and then immediately start to check whether your machine learning algorithm works well. It can automatically recognize the type of dataset and returns the informations in corresponding structure.
	"""
	
	cran = "readmnist" 

	version("1.0.6", md5="bc44e81b322da5e5cfea30b9226a0587")

