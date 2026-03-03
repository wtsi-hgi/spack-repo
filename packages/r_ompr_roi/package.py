# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROmprRoi(RPackage):
	"""A Solver for 'ompr' that Uses the R Optimization Infrastructure
('ROI')

	A solver for 'ompr' based on the R Optimization Infrastructure ('ROI').
  The package makes all solvers in 'ROI' available to solve 'ompr' models. Please see the
  'ompr' website <https://dirkschumacher.github.io/ompr/> and package docs for more information
  and examples on how to use it.
	"""
	
	homepage = "https://github.com/dirkschumacher/ompr.roi"
	cran = "ompr.roi" 

	version("1.0.2", md5="b09bf5d68e2d4837964e6a37c4eca4cf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-roi@0.3:", type=("build", "run"))
	depends_on("r-slam", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-ompr@1.0.1:", type=("build", "run"))
