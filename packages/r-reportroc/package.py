# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReportroc(RPackage):
	"""An Easy Way to Report ROC Analysis

	Provides an easy way to report the results of ROC analysis, including:
    1. an ROC curve. 
    2. the value of Cutoff, AUC (Area Under Curve), ACC (accuracy),
    SEN (sensitivity), SPE (specificity),
    PLR (positive likelihood ratio), NLR (negative likelihood ratio),
    PPV (positive predictive value), NPV (negative predictive value),
    PPA (percentage of positive accordance), NPA (percentage of negative accordance), TPA (percentage of total accordance),
    KAPPA (kappa value).
	"""
	
	cran = "reportROC" 

	version("3.6", md5="4ff1ee362a1f15a619a43a8be5679b33")

	depends_on("r-proc", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
