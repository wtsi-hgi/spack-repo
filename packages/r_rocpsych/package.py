# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocpsych(RPackage):
	"""Compute and Compare Diagnostic Test Statistics Across Groups

	Functions for (1) computing diagnostic test statistics (sensitivity, specificity, etc.) from confusion matrices with adjustment for various base rates or known prevalence based on McCaffrey et al (2003) <doi:10.1007/978-1-4615-0079-7_1>, (2) computing optimal cut-off scores with different criteria including maximizing sensitivity, maximizing specificity, and maximizing the Youden Index from Youden (1950) <https://acsjournals.onlinelibrary.wiley.com/doi/abs/10.1002/1097-0142%281950%293%3A1%3C32%3A%3AAID-CNCR2820030106%3E3.0.CO%3B2-3>, and (3) displaying and comparing classification statistics and area under the receiver operating characteristic (ROC) curves or area under the curves (AUC) across consecutive categories for ordinal variables.    
	"""
	
	cran = "ROCpsych" 

	version("1.3", md5="86e818471835d0b4409983a097ca7b3a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-reportroc", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
