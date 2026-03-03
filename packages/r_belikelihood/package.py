# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBelikelihood(RPackage):
	"""Likelihood Method for Evaluating Bioequivalence

	A likelihood method is implemented to present evidence for evaluating bioequivalence (BE). The functions use bioequivalence data [area under the blood concentration-time curve (AUC) and peak concentration (Cmax)] from various crossover designs commonly used in BE studies including a fully replicated, a partially replicated design, and a conventional 2x2 crossover design. They will calculate the profile likelihoods for the mean difference, total standard deviation ratio, and within subject standard deviation ratio for a test and a reference drug. A plot of a standardized profile likelihood can be generated along with the maximum likelihood estimate and likelihood intervals, which present evidence for bioequivalence. See Liping Du and Leena Choi (2015) <doi:10.1002/pst.1661>.
	"""
	
	cran = "BElikelihood" 

	version("1.1", md5="30b7c4e348578d7d0694af0041e50386")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
