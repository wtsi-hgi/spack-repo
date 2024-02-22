# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlyr(RPackage):
	"""Tools for Splitting, Applying and Combining Data.

	A set of tools that solves a common set of problems: you need to break a
	big problem down into manageable pieces, operate on each piece and then put
	all the pieces back together. For example, you might want to fit a model to
	each spatial location or time point in your study, summarise data by panels
	or collapse high-dimensional arrays to simpler summary statistics. The
	development of 'plyr' has been generously supported by 'Becton
	Dickinson'."""

	cran = "plyr"

	version("1.8.9", md5="5a8b129534abace172059ecc5c0b5072")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
