# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScape(RPackage):
	"""Statistical Catch-at-Age Plotting Environment

	Import, plot, and diagnose results from statistical
  catch-at-age models, used in fisheries stock assessment.
	"""
	
	cran = "scape" 

	version("2.3.3", md5="b7207162da032a148ebcc107a8fe59e5")

	depends_on("r-coda", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
