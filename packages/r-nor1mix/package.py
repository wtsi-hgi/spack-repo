# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNor1mix(RPackage):
	"""Normal aka Gaussian (1-d) Mixture Models (S3 Classes and Methods).

	One dimensional Normal Mixture Models Classes, for, e.g., density
	estimation or clustering algorithms research and teaching; providing the
	widely used Marron-Wand densities. Efficient random number generation and
	graphics; now fitting to data by ML (Maximum Likelihood) or EM
	estimation."""

	cran = "nor1mix"

	version("1.3-2", md5="2309fce297cbfb80b367b7c7f7cf007e")

