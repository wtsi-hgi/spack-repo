# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQpnca(RPackage):
	"""Noncompartmental Pharmacokinetic Analysis by qPharmetra

	Computes noncompartmental pharmacokinetic parameters
 for drug concentration profiles.  For each profile, data
 imputations and adjustments are made as necessary and
 basic parameters are estimated. Supports single dose, multi-dose,
 and multi-subject data.  Supports steady-state calculations
 and various routes of drug administration. See ?qpNCA and vignettes.
 Methodology follows Rowland and Tozer (2011, ISBN:978-0-683-07404-8), 
 Gabrielsson and Weiner (1997, ISBN:978-91-9765-100-4), and
 Gibaldi and Perrier (1982, ISBN:978-0824710422).
	"""
	
	cran = "qpNCA" 

	version("1.1.6", md5="d8e8ed137a610075e597fcaa7a4bf066")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-tidyr@0.8.2:", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
