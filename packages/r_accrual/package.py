# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAccrual(RPackage):
	"""Bayesian Accrual Prediction

	Participant recruitment for medical research is challenging. Slow accrual leads to delays in research. Accrual monitoring during the process of recruitment is critical. Researchers need reliable tools to manage the accrual rate. We developed a Bayesian method that integrates the researcher's experience with previous trials and data from the current study, providing reliable predictions on accrual rate for clinical studies. For more details and background on these methodologies, see the publications of Byron, Stephen and Susan (2008) <doi:10.1002/sim.3128>, and Yu et al. (2015) <doi:10.1002/sim.6359>. In this R package, Bayesian accrual prediction functions are presented, which can be easily used by statisticians and clinical researchers.
	"""
	
	cran = "accrual" 

	version("1.4", md5="699f66e0c5e439d3b68244f01f0a7b71")

	depends_on("r@3.1.3:", type=("build", "run"))
	depends_on("r-tcltk2", type=("build", "run"))
	depends_on("r-fgui", type=("build", "run"))
	depends_on("r-smpracticals", type=("build", "run"))
