# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTeachnet(RPackage):
	"""Fits Neural Networks to Learn About Backpropagation

	Can fit neural networks with up to two hidden layer and two different error functions. Also able to handle a weight decay. But just able to compute one output neuron and very slow. 
	"""
	
	cran = "TeachNet" 

	version("0.7.1", md5="9055a44fe8c6c2b9d912dfb3957ff1b3")

