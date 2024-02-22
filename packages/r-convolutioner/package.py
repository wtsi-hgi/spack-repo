# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RConvolutioner(RPackage):
	"""Convolution of Data

	General functions for convolutions of data. Moving average, running median, and other filters are available.
    Bibliography regarding the functions can be found in the following text.
    Richard G. Brereton (2003) <ISBN:9780471489771>.
	"""
	
	cran = "Convolutioner" 

	version("0.1.0", md5="7609d9d9101adeee4f9fbf9066e7b90f")

