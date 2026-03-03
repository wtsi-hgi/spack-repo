# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMimsunit(RPackage):
	"""Algorithm to Compute Monitor Independent Movement Summary Unit
(MIMS-Unit)

	The MIMS-unit algorithm is developed to compute Monitor Independent
    Movement Summary Unit, a measurement to summarize raw accelerometer data 
    while ensuring harmonized results across different devices. It also includes
    scripts to reproduce results in the related publication 
    (John, D., Tang. Q., Albinali, F. and Intille, S. (2019) <doi:10.1123/jmpb.2018-0068>).
	"""
	
	homepage = "https://mhealthgroup.github.io/MIMSunit/"
	cran = "MIMSunit" 

	version("0.11.2", md5="ad0d245a11f59409db5c4cf0678f0e14")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-catools@1.17.1.1:", type=("build", "run"))
	depends_on("r-tibble@3.0.4:", type=("build", "run"))
	depends_on("r-dplyr@0.7.7:", type=("build", "run"))
	depends_on("r-lubridate@1.7.4:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
	depends_on("r-plyr@1.8.4:", type=("build", "run"))
	depends_on("r-readr@1.1.1:", type=("build", "run"))
	depends_on("r-r-utils@2.7:", type=("build", "run"))
	depends_on("r-stringr@1.3.1:", type=("build", "run"))
	depends_on("r-xts@0.11.2:", type=("build", "run"))
	depends_on("r-signal@0.7.7:", type=("build", "run"))
	depends_on("r-dygraphs@1.1.1.6:", type=("build", "run"))
	depends_on("r-shiny@1.4.0.2:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.2.1:", type=("build", "run"))
