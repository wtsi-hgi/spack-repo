# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginGwrm(RPackage):
	"""R Commander Plug-in for Fitting Generalized Waring Regression
Models

	Provides an Rcmdr "plug-in" based on the GWRM package.
	"""
	
	cran = "RcmdrPlugin.GWRM" 

	version("1.0.2", md5="df66175f6d68862c421bc7a5eee413f8")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-gwrm@2.1.0.1:", type=("build", "run"))
	depends_on("r-rcmdrmisc@1.0.2:", type=("build", "run"))
	depends_on("r-rcmdr@2.0.0:", type=("build", "run"))
