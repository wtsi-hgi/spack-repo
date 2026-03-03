# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRngsetseed(RPackage):
	"""Seeding the Default RNG with a Numeric Vector

	A function setVectorSeed() is provided. Its argument
        is a numeric vector of an arbitrary nonzero length, whose
        components have integer values from [0, 2^32-1]. The input
        vector is transformed using AES (Advanced Encryption Standard)
        algorithm into an initial state of Mersenne-Twister random
        number generator. The function provides a better alternative
        to the R base function set.seed(), if the input vector is
        a single integer. Initializing a stream of random numbers
        with a vector is a convenient way to obtain several streams,
        each of which is identified by several integer indices.
	"""
	
	cran = "rngSetSeed" 

	version("0.3-3", md5="6710697b4dd1e2a3811264c70c642901")

