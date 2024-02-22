# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)


from spack.package import *


class RFda(RPackage):
	"""Functional Data Analysis.

	These functions were developed to support functional data
	analysis as described in Ramsay, J. O. and Silverman, B. W. (2005)
	Functional Data Analysis. New York: Springer and in Ramsay, J. O.,
	Hooker, Giles, and Graves, Spencer (2009)."""

	cran = "fda"

	version("6.1.4", md5="1bc4879d3e1e63171f39b05a4aca6d49")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fds", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
