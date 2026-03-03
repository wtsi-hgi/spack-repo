# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDensparcorr(RPackage):
	"""Dens-Based Method for Partial Correlation Estimation in Large
Scale Brain Networks

	Provide a Dens-based method for estimating functional connection in large scale brain networks using partial correlation.
	"""
	
	cran = "DensParcorr" 

	version("1.1", md5="8b7ac6b19fad826f40330a20a59d426c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-clime", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
