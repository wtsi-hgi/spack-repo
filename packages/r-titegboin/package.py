# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTitegboin(RPackage):
	"""Time-to-Event Dose-Finding Design for Multiple Toxicity Grades

	In some phase I trials, the design goal is to find the dose associated with a certain target toxicity rate or the dose with a certain weighted sum of rates of various toxicity grades. 'TITEgBOIN' provides the set up and calculations needed to run a dose-finding trial using bayesian optimal interval (BOIN) (Yuan et al. (2016) <doi:10.1158/1078-0432.CCR-16-0592>), generalized bayesian optimal interval (gBOIN) (Mu et al. (2019) <doi:10.1111/rssc.12263>), time-to-event bayesian optimal interval (TITEBOIN) (Lin et al. (2020) <doi:10.1093/biostatistics/kxz007>) and time-to-event generalized bayesian optimal interval (TITEgBOIN) (Takeda et al. (2022) <doi:10.1002/pst.2182>) designs. 'TITEgBOIN' can conduct tasks: run simulations and get operating characteristics; determine the dose for the next cohort; select maximum tolerated dose (MTD). These functions allow customization of design characteristics to vary sample size, cohort sizes, target dose limiting toxicity (DLT) rates or target normalized equivalent toxicity score (ETS) rates to account for discrete toxicity score, and incorporate safety and/or stopping rules.
	"""
	
	cran = "TITEgBOIN" 

	version("0.3.0", md5="8d0c15a04f7f40393e04cdf650aeb7e4")

