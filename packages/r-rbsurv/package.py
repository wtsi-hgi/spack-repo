# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbsurv(RPackage):
	"""Robust likelihood-based survival modeling with microarray data

	This package selects genes associated with survival.
	"""
	
	homepage = "http://www.korea.ac.kr/~stat2242/"
	bioc = "rbsurv"

	version("2.66.0", commit="1faecb8faba37fad2dad80b979947a0d8bcf86a6")
	version("2.60.0", commit="b2479b0f576a54092c4bb0548e9afb847f1974b6")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-biobase@2.5.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
