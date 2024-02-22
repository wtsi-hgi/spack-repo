# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrobenchmark(RPackage):
	"""Accurate Timing Functions.

	Provides infrastructure to accurately measure and compare the execution
	time of R expressions."""

	cran = "microbenchmark"

	version("1.4.10", md5="c64e467a01e792461a5cc544eac12f15")

