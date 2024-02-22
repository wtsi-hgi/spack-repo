# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrc(RPackage):
	"""Analysis of Dose-Response Curves

	Analysis of dose-response data is made available through a suite of flexible and versatile model fitting and after-fitting functions.
	"""
	
	homepage = "http://www.r-project.org"
	cran = "drc" 

	version("3.0-1", md5="50429c71d876eabdb399a81f1b5913a1")

	depends_on("r@2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
