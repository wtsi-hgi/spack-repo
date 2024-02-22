# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatda(RPackage):
	"""Statistical Analysis for Environmental Data

	Statistical analysis methods for environmental data are implemented. There is a particular focus on robust methods, and on methods for compositional data. In addition, larger data sets from geochemistry are provided. The statistical methods are described in Reimann, Filzmoser, Garrett, Dutter (2008, ISBN:978-0-470-98581-6).
	"""
	
	homepage = "http://cstat.tuwien.ac.at/filz/"
	cran = "StatDA" 

	version("1.7.11", md5="2a6e27f79e11e8df1c74feb3723d35e0")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-sgeostat", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mba", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-sp", type=("build", "run"))
	depends_on("r-geor", type=("build", "run"))
