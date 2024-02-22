# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNeoniso(RPackage):
	"""Tools to Calibrate and Work with NEON Atmospheric Isotope Data

	Functions for downloading,
    calibrating, and analyzing atmospheric isotope data bundled
    into the eddy covariance data products of the National Ecological
    Observatory Network (NEON) <https://www.neonscience.org>. 
    Calibration tools are provided for carbon and water isotope products.
    Carbon isotope calibration details are found in Fiorella et al. (2021)
    <doi:10.1029/2020JG005862>, and the readme 
    file at <https://github.com/lanl/NEONiso>. Tools for calibrating water 
    isotope products have been added as of 0.6.0, but have known deficiencies
    and should be considered very experimental currently.
	"""
	
	homepage = "https://github.com/lanl/NEONiso"
	cran = "NEONiso" 

	version("0.6.4", md5="9ebfc6a3df9f9ea03bbdea4c3fdfff9c")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-neonutilities@2.0.1:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rhdf5@2.33.7:", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-tidyselect", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
