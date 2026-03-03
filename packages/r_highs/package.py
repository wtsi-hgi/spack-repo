# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighs(RPackage):
	"""'HiGHS' Optimization Solver

	R interface to 'HiGHS', an optimization solver for solving mixed integer 
        optimization problems with quadratic or linear objective and linear constraints.
	"""
	
	homepage = "https://gitlab.com/roigrp/solver/highs"
	cran = "highs" 

	version("0.1-10", md5="05e4ff7c910e5bf8cd170e247986bd11")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("bash", type=("build", "link", "run"))
	depends_on("pkgconfig", type=("build", "link", "run"))
	depends_on("cmake@3.1.6:", type=("build", "link", "run"))
