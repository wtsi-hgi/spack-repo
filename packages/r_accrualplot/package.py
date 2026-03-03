# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccrualplot(RPackage):
	"""Accrual Plots and Predictions for Clinical Trials

	Tracking accrual in clinical trials is important for trial success. 
    If accrual is too slow, the trial will take too long and be too expensive. If
    accrual is much faster than expected, time sensitive tasks such as the writing 
    of statistical analysis plans might need to be rushed. 'accrualPlot' provides 
    functions to aid the tracking of accrual and predict when a trial will reach 
    it's intended sample size.
	"""
	
	homepage = "https://github.com/CTU-Bern/accrualPlot"
	cran = "accrualPlot" 

	version("1.0.7", md5="55fb9c4dabd8ee55a686979729f5289b")

	depends_on("r-lubridate", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
