# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyclomort(RPackage):
	"""Survival Modeling with a Periodic Hazard Function

	Modeling periodic mortality (or other time-to event) processes from right-censored data. Given observations of a process with a known period (e.g. 365 days, 24 hours), functions determine the number, intensity, timing, and duration of peaks of periods of elevated hazard within a period.  The underlying model is a mixed wrapped Cauchy function fitted using maximum likelihoods (details in Gurarie et al. (2020) <doi:10.1111/2041-210X.13305>). The development of these tools was motivated by the strongly seasonal mortality patterns observed in many wild animal populations, such that the respective periods of higher mortality can be identified as "mortality seasons". 
	"""
	
	homepage = "https://github.com/EliGurarie/cyclomort"
	cran = "cyclomort" 

	version("1.0.2", md5="f7db13ca90cf1e5a05ce9fb7e5601850")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
