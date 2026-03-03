# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcsshiny(RPackage):
	"""ICS via a Shiny Application

	Performs Invariant Coordinate Selection (ICS) (Tyler, Critchley, Duembgen and Oja (2009) <doi:10.1111/j.1467-9868.2009.00706.x>) and especially ICS for multivariate outlier detection with application to quality control (Archimbaud, Nordhausen, Ruiz-Gazen (2016) <arXiv:1612.06118>) using a shiny app.
	"""
	
	cran = "ICSShiny" 

	version("0.5", md5="3389c12e5a6bb656027d00571bbdff82")

	depends_on("r-ics", type=("build", "run"))
	depends_on("r-icsoutlier", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-icsnp", type=("build", "run"))
	depends_on("r-rrcov", type=("build", "run"))
	depends_on("r-simsalapar", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
