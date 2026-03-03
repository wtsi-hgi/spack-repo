# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJointvip(RPackage):
	"""Prioritize Variables with Joint Variable Importance Plot in
Observational Study Design

	In the observational study design stage, matching/weighting methods are
    conducted. However, when many background variables are present, the decision as to 
    which variables to prioritize for matching/weighting is not trivial. Thus, the 
    joint treatment-outcome variable importance plots are created to guide variable
    selection. The joint variable importance plots enhance variable comparisons via
    unadjusted bias curves derived under the omitted variable bias framework. The 
    plots translate variable importance into recommended values for tuning parameters 
    in existing methods. Post-matching and/or weighting plots can also be used to 
    visualize and assess the quality of the observational study design. The method 
    motivation and derivation is presented in "Using Joint Variable Importance Plots 
    to Prioritize Variables in Assessing the Impact of Glyburide on Adverse Birth 
    Outcomes" by Liao et al. (2023) <arXiv:2301.09754>. See the package paper by Liao 
    and Pimentel (2023) <arxiv:2302.10367> for a beginner friendly user introduction.
	"""
	
	homepage = "https://github.com/ldliao/jointVIP"
	cran = "jointVIP" 

	version("0.1.2", md5="3cd0c1275ca5221c1101aec6f04bdee6")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggrepel@0.9.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
