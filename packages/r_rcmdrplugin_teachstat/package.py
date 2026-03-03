# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginTeachstat(RPackage):
	"""R Commander Plugin for Teaching Statistical Methods

	R Commander plugin for teaching statistical methods. 
    It adds a new menu for making easier the teaching of the main concepts about the main statistical methods.
	"""
	
	cran = "RcmdrPlugin.TeachStat" 

	version("1.1.3", md5="7779bde897e3c57ba2568986d25b21c9")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcmdr@2.5.1:", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-indexnumr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-distr", type=("build", "run"))
	depends_on("r-distrex", type=("build", "run"))
