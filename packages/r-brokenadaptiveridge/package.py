# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBrokenadaptiveridge(RPackage):
	"""Broken Adaptive Ridge Regression with Cyclops

	Approximates best-subset selection (L0) regression with
   an iteratively adaptive Ridge (L2) penalty for large-scale models.
   This package uses Cyclops for an efficient implementation and the
   iterative method is described in Kawaguchi et al (2020)
   <doi:10.1002/sim.8438> and Li et al (2021)
   <doi:10.1016/j.jspi.2020.12.001>.
	"""
	
	cran = "BrokenAdaptiveRidge" 

	version("1.0.0", md5="727587b767be591615934e7ace33c253")

	depends_on("r@3.2.2:", type=("build", "run"))
	depends_on("r-cyclops@3:", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
