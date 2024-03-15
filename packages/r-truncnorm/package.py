# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruncnorm(RPackage):
	"""Truncated Normal Distribution.

	Density, probability, quantile and random number generation functions for
	the truncated normal distribution."""

	cran = "truncnorm"

	license("GPL-2.0-or-later")

	version("1.0-9", md5="878c944c50c6eeaea3e4e6d9586216d3")

	depends_on("r@3.4:", type=("build", "run"))
