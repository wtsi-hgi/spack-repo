# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNp(RPackage):
	"""Nonparametric Kernel Smoothing Methods for Mixed Data Types.

	This package provides a variety of nonparametric (and semiparametric)
	kernel methods that seamlessly handle a mix of continuous, unordered, and
	ordered factor data types. We would like to gratefully acknowledge support
	from the Natural Sciences and Engineering Research Council of Canada
	(NSERC:www.nserc.ca), the Social Sciences and Humanities Research Council
	of Canada (SSHRC:www.sshrc.ca), and the Shared Hierarchical Academic
	Research Computing Network (SHARCNET:www.sharcnet.ca)."""

	cran = "np"

	version("0.60-17", md5="2d33c39b0b35e70b3ae14cd73111c847")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-cubature", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
