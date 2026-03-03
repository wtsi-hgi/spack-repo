# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrepdat(RPackage):
	"""Preparing Experimental Data for Statistical Analysis

	Prepares data for statistical analysis (e.g., analysis of variance
  ;ANOVA) by enabling the user to easily and quickly merge (using the
  file_merge() function) raw data files into one merged table and then
  aggregate the merged table (using the prep() function) into a finalized
  table while keeping track and summarizing every step of the preparation.
  The finalized table contains several possibilities for dependent measures of
  the dependent variable. Most suitable when measuring variables in an
  interval or ratio scale (e.g., reaction-times) and/or discrete values such
  as accuracy. Main functions included are file_merge() and prep(). The
  file_merge() function vertically merges individual data files (in a long
  format) in which each line is a single observation to one single dataset.
  The prep() function aggregates the single dataset according to any
  combination of grouping variables (i.e., between-subjects and
  within-subjects independent variables, respectively), and returns a data
  frame with a number of dependent measures for further analysis for each cell
  according to the combination of provided grouping variables. Dependent
  measures for each cell include among others means before and after rejecting
  all values according to a flexible standard deviation criteria, number of
  rejected values according to the flexible standard deviation criteria,
  proportions of rejected values according to the flexible standard deviation
  criteria, number of values before rejection, means after rejecting values
  according to procedures described in Van Selst & Jolicoeur (1994; suitable
  when measuring reaction-times), standard deviations, medians, means according
  to any percentile (e.g., 0.05, 0.25, 0.75, 0.95) and harmonic means. The data
  frame prep() returns can also be exported as a txt file to be used for
  statistical analysis in other statistical programs.
	"""
	
	homepage = "http://github.com/ayalaallon/prepdat"
	cran = "prepdat" 

	version("1.0.8", md5="9a8f96cf019d6504a00f154c8d16b2bd")

	depends_on("r@3.0.3:", type=("build", "run"))
	depends_on("r-dplyr@0.4.2:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-psych@1.5.4:", type=("build", "run"))
