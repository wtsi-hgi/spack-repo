# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REbprs(RPackage):
	"""Derive Polygenic Risk Score Based on Emprical Bayes Theory

	EB-PRS is a novel method that leverages information for effect sizes across all the markers to improve the prediction accuracy.  No parameter tuning is needed in the method, and no external information is needed. This R-package provides the calculation of polygenic risk scores from the given training summary statistics and testing data. We can use EB-PRS to extract main information, estimate Empirical Bayes parameters, derive polygenic risk scores for  each individual in testing data, and evaluate the PRS according to AUC and predictive r2. See Song et al. (2020) <doi:10.1371/journal.pcbi.1007565> for a detailed presentation of the method.
	"""
	
	cran = "EBPRS" 

	version("2.1.0", md5="000f2415379e1b284b453a7b36b56c86")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rocr", type=("build", "run"))
	depends_on("r-bedmatrix", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
