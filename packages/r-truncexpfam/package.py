# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTruncexpfam(RPackage):
	"""Truncated Exponential Family

	Handles truncated members from the exponential family of
	probability distributions. Contains functions such as rtruncnorm() and
	dtruncpois(), which are truncated versions of rnorm() and dpois() from the
	stats package that also offer richer output containing, for example, the
	distribution parameters. It also provides functions to retrieve the original
	distribution parameters from a truncated sample by maximum-likelihood
	estimation.
	"""
	
	homepage = "https://ocbe-uio.github.io/TruncExpFam/"
	cran = "TruncExpFam" 

	version("1.1.0", md5="f09c7c1a95b454dd088292e6bb44e85b")

	depends_on("r-invgamma", type=("build", "run"))
	depends_on("r-rmutil", type=("build", "run"))
