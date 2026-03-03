# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAqeval(RPackage):
	"""Air Quality Evaluation

	Developed for use by those tasked with the routine detection,
         characterisation and quantification of discrete changes in air quality
         time-series, such as identifying the impacts of air quality policy
         interventions. The main functions use signal isolation then
         break-point/segment (BP/S) methods based on 'strucchange' and 'segmented'
         methods to detect and quantify change events (Ropkins & Tate, 2021,
         <doi:10.1016/j.scitotenv.2020.142374>).
	"""
	
	homepage = "https://github.com/karlropkins/AQEval"
	cran = "AQEval" 

	version("0.5.2", md5="aa510566a00b6cb06adf44927c2f4c24")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-openair", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-loa", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-strucchange", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-ggtext", type=("build", "run"))
