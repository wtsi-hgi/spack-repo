# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRlecuyer(RPackage):
	"""R Interface to RNG with Multiple Streams

	Provides an interface to the C implementation of the
        random number generator with multiple independent streams
        developed by L'Ecuyer et al (2002). The main purpose of this
        package is to enable the use of this random number generator in
        parallel R applications.
	"""
	
	homepage = "http://www.iro.umontreal.ca/~lecuyer/myftp/papers/streams00.pdf"
	cran = "rlecuyer" 

	version("0.3-8", md5="62483448f69d36e38a39e3339469478b")

