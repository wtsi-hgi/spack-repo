# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStabm(RPackage):
	"""Stability Measures for Feature Selection

	An implementation of many measures for the
    assessment of the stability of feature selection. Both simple measures
    and measures which take into account the similarities between features
    are available, see Bommert (2020) <doi:10.17877/DE290R-21906>.
	"""
	
	homepage = "https://bommert.github.io/stabm/"
	cran = "stabm" 

	version("1.2.2", md5="081eb85f2e2ce1bf921f21903d7554e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate@1.8.5:", type=("build", "run"))
	depends_on("r-matrix@1.5.0:", type=("build", "run"))
