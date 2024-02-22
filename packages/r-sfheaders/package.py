# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSfheaders(RPackage):
	"""Converts Between R Objects and Simple Feature Objects.

	Converts between R and Simple Feature 'sf' objects, without depending on
	the Simple Feature library. Conversion functions are available at both the
	R level, and through 'Rcpp'."""

	cran = "sfheaders"

	version("0.4.4", md5="28bd3e7fe95ab6d9d41c27d6f153c443")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-geometries@0.2.4:", type=("build", "run"))
