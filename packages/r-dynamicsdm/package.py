# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDynamicsdm(RPackage):
	"""Species Distribution and Abundance Modelling at High
Spatio-Temporal Resolution

	A collection of novel tools for generating species distribution and abundance models (SDM) that are dynamic through both space and time. These highly flexible functions incorporate spatial and temporal aspects across key SDM stages; including when cleaning and filtering species occurrence data, generating pseudo-absence records, assessing and correcting sampling biases and autocorrelation, extracting explanatory variables and projecting distribution patterns. Throughout, functions utilise Google Earth Engine and Google Drive to minimise the computing power and storage demands associated with species distribution modelling at high spatio-temporal resolution.
	"""
	
	homepage = "https://github.com/r-a-dobson/dynamicSDM"
	cran = "dynamicSDM" 

	version("1.3.3", md5="df010088a4ccc6bd5cfe90de8c874f6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-googledrive", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
	depends_on("r-rgee", type=("build", "run"))
	depends_on("r-terra", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-sf", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
