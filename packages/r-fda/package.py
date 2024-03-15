# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
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

	license("GPL-2.0-or-later")

	version("6.1.8", md5="fb851a29a27b2166904b8b9fdf1f9f2b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-fds", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
