# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChopthin(RPackage):
	"""The Chopthin Resampler

	Resampling is a standard step in particle filtering and in
    sequential Monte Carlo. This package implements the chopthin resampler, which
    keeps a bound on the ratio between the largest and the smallest weights after
    resampling.
	"""
	
	cran = "chopthin" 

	version("0.2.2", md5="e95c3420b74889461ba26556490dd91b")

	depends_on("r-rcpp", type=("build", "run"))
