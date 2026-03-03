# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTurboem(RPackage):
	"""A Suite of Convergence Acceleration Schemes for EM, MM and Other
Fixed-Point Algorithms

	Algorithms for accelerating the convergence of slow,
        monotone sequences from smooth, contraction mapping such as the
        EM and MM algorithms. It can be used to accelerate any smooth,
        linearly convergent acceleration scheme.  A tutorial style
        introduction to this package is available in a vignette on the
        CRAN download page or, when the package is loaded in an R
        session, with vignette("turboEM").
	"""
	
	homepage = "https://coah.jhu.edu/people/Faculty_personal_Pages/Varadhan.html"
	cran = "turboEM" 

	version("2021.1", md5="48be670dfe0197c7f24e9251f5159881")

	depends_on("r@2.12:", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-iterators", type=("build", "run"))
