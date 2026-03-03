# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLfstat(RPackage):
	"""Calculation of Low Flow Statistics for Daily Stream Flow Data

	The "Manual on Low-flow Estimation and Prediction" (Gustard & Demuth (2009, ISBN:978-92-63-11029-9)), published by the World Meteorological Organisation, gives a comprehensive summary on how to analyse stream flow data focusing on low-flows. This packages provides functions to compute the described statistics and produces plots similar to the ones in the manual. 
	"""
	
	cran = "lfstat" 

	version("0.9.12", md5="475b5f13fd02fcf27ae47e2ad670648f")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-xts", type=("build", "run"))
	depends_on("r-lmom", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-lmomrfa", type=("build", "run"))
	depends_on("r-dygraphs", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-latticeextra", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
