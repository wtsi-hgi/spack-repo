# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RR4lineups(RPackage):
	"""Statistical Inference on Lineup Fairness

	Since the early 1970s eyewitness testimony researchers have recognised the 
    importance of estimating properties such as lineup bias (is the lineup biased against 
    the suspect, leading to a rate of choosing higher than one would expect by chance?), 
    and lineup size (how many reasonable choices are in fact available to the witness? 
    A lineup is supposed to consist of a suspect and a number of additional members, 
    or foils, whom a poor-quality witness might mistake for the perpetrator). Lineup 
    measures are descriptive, in the first instance, but since the earliest articles in 
    the literature researchers have recognised the importance of reasoning inferentially 
    about them. This package contains functions to compute various properties of 
    laboratory or police lineups, and is intended for use by researchers in forensic 
    psychology and/or eyewitness testimony research. Among others, the r4lineups package 
    includes functions for calculating lineup proportion, functional size, various 
    estimates of effective size, diagnosticity ratio, homogeneity of the diagnosticity 
    ratio, ROC curves for confidence x accuracy data and the degree of similarity of 
    faces in a lineup. 
	"""
	
	cran = "r4lineups" 

	version("0.1.1", md5="e57fde81779ccd1f990426b0ad85d6d3")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-here", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-proc", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
