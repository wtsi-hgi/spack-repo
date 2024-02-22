# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeifly(RPackage):
	"""Interactive Model Exploration using 'GGobi'

	Exploratory model analysis with <http://ggobi.org>.  
    Fit and graphical explore ensembles of linear models.
	"""
	
	homepage = "https://github.com/hadley/meifly"
	cran = "meifly" 

	version("0.3.1", md5="f218f45b3a848e528d7040f218616e00")

	depends_on("r-leaps", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
