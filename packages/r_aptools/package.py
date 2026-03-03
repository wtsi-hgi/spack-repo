# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAptools(RPackage):
	"""Average Positive Predictive Values (AP) for Binary Outcomes and
Censored Event Times

	We provide tools to estimate two prediction accuracy metrics,
    the average positive predictive values (AP) as well as the well-known AUC
    (the area under the receiver operator characteristic curve) for risk scores. 
    The outcome of interest is either binary or censored event time.
    Note that for censored event time, our functions' estimates, the AP and the
    AUC, are time-dependent for pre-specified time interval(s). A function that
    compares the APs of two risk scores/markers is also included. Optional
    outputs include positive predictive values and true positive fractions at
    the specified marker cut-off values, and a plot of the time-dependent AP
    versus time (available for event time data).
	"""
	
	cran = "APtools" 

	version("6.8.8", md5="f2929b5551ee6f7218ff873a959b13ec")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-cmprsk", type=("build", "run"))
