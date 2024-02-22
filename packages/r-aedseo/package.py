# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAedseo(RPackage):
	"""Automated and Early Detection of Seasonal Epidemic Onset

	A powerful tool for automating the early detection of seasonal epidemic
             onsets in time series data. It offers the ability to estimate growth rates
             for consecutive time intervals and calculate the sum of cases (SoC) within 
             those intervals. It is particularly useful for epidemiologists, public 
             health professionals, and researchers seeking to identify and respond to 
             seasonal epidemics in a timely fashion.
             For reference on growth rate estimation, see Walling and Lipstich (2007) 
             <doi:10.1098/rspb.2006.3754> and Obadia et al. (2012) <doi:10.1186/1472-6947-12-147>.
	"""
	
	homepage = "https://github.com/ssi-dk/aedseo"
	cran = "aedseo" 

	version("0.1.2", md5="39126fd14b0fd5bf8ddaa566db464a30")

	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
