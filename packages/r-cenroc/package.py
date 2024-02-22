# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCenroc(RPackage):
	"""Estimating Time-Dependent ROC Curve and AUC for Censored Data

	Contains functions to estimate a smoothed and a non-smoothed (empirical) time-dependent 
             receiver operating characteristic curve and the corresponding area under the receiver 
             operating characteristic curve and the optimal cutoff point for the right and interval 
             censored survival data. See Beyene and El Ghouch (2020)<doi:10.1002/sim.8671> and Beyene 
             and El Ghouch (2022) <doi:10.1002/bimj.202000382>.
	"""
	
	cran = "cenROC" 

	version("2.0.0", md5="76eb9a2446d6a03cfd6bf979f1c1f826")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-icenreg", type=("build", "run"))
	depends_on("r-condsurv", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
