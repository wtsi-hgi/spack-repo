# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDebest(RPackage):
	"""Duration Estimation for Biomarker Enrichment Studies and Trials

	A general framework using mixture Weibull distributions to accurately predict biomarker-guided trial duration accounting for heterogeneous population. Extensive simulations are performed to evaluate the impact of heterogeneous population and the dynamics of biomarker characteristics and disease on the study duration. Several influential parameters including median survival time, enrollment rate, biomarker prevalence and effect size are identified. Efficiency gains of biomarker-guided trials can be quantitatively compared to the traditional all-comers design. For reference, see Zhang et al. (2024) <arXiv:2401.00540>.
	"""
	
	cran = "debest" 

	version("0.1.0", md5="290e485f131a2910b1bec26ad95753b2")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-flexsurv", type=("build", "run"))
