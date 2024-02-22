# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RComplexnet(RPackage):
	"""Complex Network Generation

	Providing a set of functions to easily generate and iterate complex networks.
 The functions can be used to generate realistic networks with a wide range of different clustering, density, and average path length.
 For more information consult research articles by Amiyaal Ilany and Erol Akcay (2016) <doi:10.1093/icb/icw068> and Ilany and Erol Akcay (2016) <doi:10.1101/026120>, which have inspired many methods in this package.
	"""
	
	homepage = "https://marcosmolla.github.io/complexNet/"
	cran = "complexNet" 

	version("0.2.0", md5="b1b3d44156e17fd4df63c52cd8d8680b")

