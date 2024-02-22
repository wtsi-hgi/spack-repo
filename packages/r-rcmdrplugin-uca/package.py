# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcmdrpluginUca(RPackage):
	"""UCA Rcmdr Plug-in

	Some extensions to Rcmdr (R Commander), randomness test, 
 variance test for one normal sample and predictions using active model, 
 made by R-UCA project and used in teaching statistics at University of Cadiz (UCA).
	"""
	
	homepage = "http://knuth.uca.es/RcmdrPlugin.UCA/"
	cran = "RcmdrPlugin.UCA" 

	version("5.1-1", md5="6e4044a89af84cbfb56bf59c4c818f1d")

	depends_on("r-iqcc", type=("build", "run"))
	depends_on("r-qcc", type=("build", "run"))
	depends_on("r-qicharts2", type=("build", "run"))
	depends_on("r-randtests", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-teachingdemos", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-rcmdr@1.6:", type=("build", "run"))
