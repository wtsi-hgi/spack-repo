# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFutility(RPackage):
	"""Interim Analysis of Operational Futility in Randomized Trials
with Time-to-Event Endpoints and Fixed Follow-Up

	Randomized clinical trials commonly follow participants for a time-to-event efficacy endpoint for a fixed period of time. Consequently, at the time when the last enrolled participant completes their follow-up, the number of observed endpoints is a random variable. Assuming data collected through an interim timepoint, simulation-based estimation and inferential procedures in the standard right-censored failure time analysis framework are conducted for the distribution of the number of endpoints--in total as well as by treatment arm--at the end of the follow-up period. The future (i.e., yet unobserved) enrollment, endpoint, and dropout times are generated according to mechanisms specified in the simTrial() function in the 'seqDesign' package. A Bayesian model for the endpoint rate, offering the option to specify a robust mixture prior distribution, is used for generating future data (see the vignette for details). Inference can be restricted to participants who received treatment according to the protocol and are observed to be at risk for the endpoint at a specified timepoint. Plotting functions are provided for graphical display of results.
	"""
	
	homepage = "https://github.com/mjuraska/futility"
	cran = "futility" 

	version("0.4", md5="cc28d22ab3c52cad6a4545a18dea3a24")

