# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROxcaar(RPackage):
	"""Interface to 'OxCal' Radiocarbon Calibration

	A set of tools that enables using 'OxCal' from within R. 'OxCal' (<https://c14.arch.ox.ac.uk/oxcal.html>) is a standard archaeological tool intended to provide 14C calibration and analysis of archaeological and environmental chronological information. 'OxcAAR' allows simple calibration with 'Oxcal' and plotting of the results as well as the execution of sophisticated ('OxCal') code and the import of the results of bulk analysis and complex Bayesian sequential calibration.
	"""
	
	cran = "oxcAAR" 

	version("1.1.1", md5="9c21aa095f2c6a790002259b85dd70a9")

	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
