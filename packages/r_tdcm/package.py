# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTdcm(RPackage):
	"""The Transition Diagnostic Classification Model Framework

	Estimate the transition diagnostic classification model (TDCM) 
    described in Madison & Bradshaw (2018) <doi:10.1007/s11336-018-9638-5>, a 
    longitudinal extension of the log-linear cognitive diagnosis model (LCDM) in 
    Henson, Templin & Willse (2009) <doi:10.1007/s11336-008-9089-5>. As the LCDM 
    subsumes many other diagnostic classification models (DCMs), many other DCMs 
    can be estimated longitudinally via the TDCM. The 'TDCM' package includes 
    functions to estimate the single-group and multigroup TDCM, summarize 
    results of interest including item parameters, growth proportions, 
    transition probabilities, transitional reliability, attribute correlations, 
    model fit, and growth plots.
	"""
	
	homepage = "https://github.com/cotterell/tdcm"
	cran = "TDCM" 

	version("0.1.0", md5="66d9483557f68ae444de4b4e43a56c09")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-cdm", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-polycor", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("pandoc", type=("build", "link", "run"))
