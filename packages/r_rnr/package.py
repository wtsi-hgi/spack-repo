# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRnr(RPackage):
	"""Rosenbaum and Rubin Sensitivity

	Apply sensitivity analysis for offline policy evaluation, as
    implemented in Jung et al. (2017) <arXiv:1702.04690> based
    on Rosenbaum and Rubin (1983) <http://www.jstor.org/stable/2345524>.
	"""
	
	cran = "rnr" 

	version("0.2.1", md5="bb039b1d5e99b179f82d81d3089884b4")

	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
