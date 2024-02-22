# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbooster(RPackage):
	"""AdaBoost Framework for Any Classifier

	This is a simple package which provides a function
      that boosts pre-ready or custom-made classifiers. Package
      uses Discrete AdaBoost (<doi:10.1006/jcss.1997.1504>) and Real AdaBoost
      (<doi:10.1214/aos/1016218223>) for two class,
      SAMME (<doi:10.4310/SII.2009.v2.n3.a8>) and
      SAMME.R (<doi:10.4310/SII.2009.v2.n3.a8>)
      for multiclass classification. 
	"""
	
	cran = "rbooster" 

	version("1.1.0", md5="fab2be0fc6dca953aea47fdf89b1b624")

	depends_on("r@4.0.4:", type=("build", "run"))
	depends_on("r-rpart", type=("build", "run"))
	depends_on("r-earth", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
