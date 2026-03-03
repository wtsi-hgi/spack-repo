# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPopdesign(RPackage):
	"""Posterior Predictive (PoP) Design for Phase I Clinical Trials

	The primary goal of phase I clinical trials is to find the maximum tolerated dose (MTD). To reach this objective, we introduce a new design for phase I clinical trials, the posterior predictive (PoP) design. The PoP design is an innovative model-assisted design that is as simply as the conventional algorithmic designs as its decision rules can be pre-tabulated prior to the onset of trial, but is of more flexibility of selecting diverse target toxicity rates and cohort sizes. The PoP design has desirable properties, such as coherence and consistency. Moreover, the PoP design provides better empirical performance than the BOIN and Keyboard design with respect to high average probabilities of choosing the MTD and slightly lower risk of treating patients at subtherapeutic or overly toxic doses. 
	"""
	
	cran = "PoPdesign" 

	version("1.0.4", md5="8f03151901ae5f4938aa4de397bbb3e8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iso", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
