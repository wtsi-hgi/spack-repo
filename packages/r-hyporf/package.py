# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHyporf(RPackage):
	"""Random Forest Two-Sample Tests

	An implementation of Random Forest-based two-sample tests as introduced in Hediger & Michel & Naef (2020) <arXiv:1903.06287>.
	"""
	
	cran = "hypoRF" 

	version("1.0.0", md5="bd214415a4b757c7fb15bd6a800592c0")

	depends_on("r-ranger", type=("build", "run"))
