# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCorpower(RPackage):
	"""Power Calculations for Assessing Correlates of Risk in Clinical
Efficacy Trials

	Calculates power for assessment of intermediate biomarker responses as correlates of risk in the active treatment group in clinical efficacy trials, as described in Gilbert, Janes, and Huang, Power/Sample Size Calculations for Assessing Correlates of Risk in Clinical Efficacy Trials (2016, Statistics in Medicine). The methods differ from past approaches by accounting for the level of clinical treatment efficacy overall and in biomarker response subgroups, which enables the correlates of risk results to be interpreted in terms of potential correlates of efficacy/protection. The methods also account for inter-individual variability of the observed biomarker response that is not biologically relevant (e.g., due to technical measurement error of the laboratory assay used to measure the biomarker response), which is important because power to detect a specified correlate of risk effect size is heavily affected by the biomarker's measurement error. The methods can be used for a general binary clinical endpoint model with a univariate dichotomous, trichotomous, or continuous biomarker response measured in active treatment recipients at a fixed timepoint after randomization, with either case-cohort Bernoulli sampling or case-control without-replacement sampling of the biomarker (a baseline biomarker is handled as a trivial special case). In a specified two-group trial design, the computeN() function can initially be used for calculating additional requisite design parameters pertaining to the target population of active treatment recipients observed to be at risk at the biomarker sampling timepoint. Subsequently, the power calculation employs an inverse probability weighted logistic regression model fitted by the tps() function in the 'osDesign' package. Power results as well as the relationship between the correlate of risk effect size and treatment efficacy can be visualized using various plotting functions. To link power calculations for detecting a correlate of risk and a correlate of treatment efficacy, a baseline immunogenicity predictor (BIP) can be simulated according to a specified classification rule (for dichotomous or trichotomous BIPs) or correlation with the biomarker response (for continuous BIPs), then outputted along with biomarker response data under assignment to treatment, and clinical endpoint data for both treatment and placebo groups.
	"""
	
	homepage = "https://github.com/mjuraska/CoRpower"
	cran = "CoRpower" 

	version("1.0.4", md5="c91a29b1a9cd13283a3612ff48f99874")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-osdesign", type=("build", "run"))
