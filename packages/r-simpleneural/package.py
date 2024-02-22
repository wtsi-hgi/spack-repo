# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimpleneural(RPackage):
	"""An Easy to Use Multilayer Perceptron

	Trains neural networks (multilayer perceptrons with one hidden layer) for bi- or multi-class classification.
	"""
	
	cran = "simpleNeural" 

	version("0.1.3", md5="bbe3b861276582cbf6fcc046c94d8201")

	depends_on("r@3.6:", type=("build", "run"))
