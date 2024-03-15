# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCfo(RPackage):
	"""CFO-Type Designs in Phase I Clinical Trials

	In phase I clinical trials, the primary objective is to ascertain the maximum tolerated dose (MTD) corresponding to a specified target toxicity rate. The 'CFO' package facilitates the implementation of dose-finding trials by utilizing calibration-free odds type (CFO-type) designs. Specifically, it encompasses the calibration-free odds (CFO) (Jin and Yin (2022) <doi:10.1177/09622802221079353>), two-dimensional CFO (2dCFO) (Wang et al. (2023) <doi:10.3389/fonc.2023.1294258>), time-to-event CFO (TITE-CFO) (Jin and Yin (2023) <doi:10.1002/pst.2304>), fractional CFO (fCFO), accumulative CFO (aCFO), TITE-aCFO, and f-aCFO designs. The ‘CFO' package accommodates diverse CFO-type designs, allowing users to tailor the approach based on factors such as dose information inclusion, handling of late-onset toxicity, and the nature of the target drug (single-drug or drug-combination). The functionalities embedded in 'CFO' package include the determination of the dose level for the next cohort, the selection of the MTD for a real trial, and the execution of single or multiple simulations to obtain operating characteristics. Moreover, these functions are equipped with early stopping and dose elimination rules to address safety considerations. Users have the flexibility to choose different distributions, thresholds, and cohort sizes among others for their specific needs. The output of the 'CFO' package can be summary statistics as well as various plots for better visualization. 
	"""
	
	cran = "CFO" 

	version("1.1.0", md5="07b9ce60ded6eaf38de91e5fd10f0a14")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
