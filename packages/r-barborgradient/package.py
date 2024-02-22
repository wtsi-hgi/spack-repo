# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBarborgradient(RPackage):
	"""Function Minimum Approximator

	Tool to find where a function has its lowest value(minimum). The
    functions can be any dimensions. Recommended use is with eps=10^-10, but can be
    run with 10^-20, although this depends on the function. Two more methods are in
    this package, simple gradient method (Gradmod) and Powell method (Powell). These
    are not recommended for use, their purpose are purely for comparison.
	"""
	
	cran = "BarBorGradient" 

	version("1.0.5", md5="479b881bee668893b6f245f492f1c1ac")

	depends_on("r@3:", type=("build", "run"))
