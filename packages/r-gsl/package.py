# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGsl(RPackage):
	"""Wrapper for the Gnu Scientific Library.

	An R wrapper for some of the functionality of the Gnu Scientific
	Library."""

	cran = "gsl"

	version("2.1-8", md5="357bceb886f42b70fb2056a401d5c401")

	depends_on("r@4:", type=("build", "run"))
	depends_on("gsl@2.5:", type=("build", "link", "run"))
