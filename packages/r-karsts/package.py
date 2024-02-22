# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKarsts(RPackage):
	"""An Interface for Microclimate Time Series Analysis

	An R code with a GUI for microclimate time series, with an emphasis on underground environments. 'KarsTS' provides linear and nonlinear methods, including recurrence analysis (Marwan et al. (2007) <doi:10.1016/j.physrep.2006.11.001>) and filling methods (Moffat et al. (2007) <doi:10.1016/j.agrformet.2007.08.011>), as well as tools to manipulate easily time series and gap sets.
	"""
	
	cran = "KarsTS" 

	version("2.4.1", md5="65209bf97ddc1ae9e68854e5e7832fb4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-circular", type=("build", "run"))
	depends_on("r-mvn", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-tserieschaos", type=("build", "run"))
	depends_on("r-stlplus", type=("build", "run"))
	depends_on("r-tseries", type=("build", "run"))
	depends_on("r-forecast", type=("build", "run"))
	depends_on("r-stinepack", type=("build", "run"))
	depends_on("r-missforest", type=("build", "run"))
	depends_on("r-nonlineartseries", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-infotheo", type=("build", "run"))
	depends_on("r-plot3d", type=("build", "run"))
