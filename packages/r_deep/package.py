# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDeep(RPackage):
	"""A Neural Networks Framework

	Explore neural networks in a layer oriented way, the framework
    is intended to give the user total control of the
    internals of a net without much effort. Use classes like PerceptronLayer
    to create a layer of Percetron neurons, and specify how many you want. The
    package does all the tricky stuff internally leaving you focused in what
    you want. I wrote this package during a neural networks course to help me
    with the problem set.
	"""
	
	cran = "deep" 

	version("0.1.0", md5="215eb37be9869aabc00eba5165b43bd3")

