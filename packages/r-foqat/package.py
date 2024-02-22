# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFoqat(RPackage):
	"""Field Observation Quick Analysis Toolkit

	Tools for quickly processing and analyzing 
	field observation data and air quality data. This 
	tools contain functions that facilitate analysis 
	in atmospheric chemistry (especially in ozone 
	pollution). Some functions of time series are also 
	applicable to other fields. For detail please view 
	homepage<https://github.com/tianshu129/foqat>.
	Scientific Reference:
	1. The Hydroxyl Radical (OH) Reactivity: Roger Atkinson and Janet Arey (2003) <doi:10.1021/cr0206420>.
	2. Ozone Formation Potential (OFP): <http://ww2.arb.ca.gov/sites/default/files/barcu/regact/2009/mir2009/mir10.pdf>, Zhang et al.(2021) <doi:10.5194/acp-21-11053-2021>.
	3. Aerosol Formation Potential (AFP): Wenjing Wu et al. (2016) <doi:10.1016/j.jes.2016.03.025>.
	4. TUV model: <https://www2.acom.ucar.edu/modeling/tropospheric-ultraviolet-and-visible-tuv-radiation-model>.
	"""
	
	homepage = "https://github.com/tianshu129/foqat"
	cran = "foqat" 

	version("2.0.8.2", md5="3d5eca0f55d6f46069eafa02bd78a7c3")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-lmodel2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggplotify", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-ggnewscale", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
