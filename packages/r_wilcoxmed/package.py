# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWilcoxmed(RPackage):
	"""Computes Values for the 1-Sample Wilcoxon Sign Rank Test for
Medians

	An implementation of the 1-Sample Wilcoxon Sign rank test for medians. 
              It includes 2 functions, W_stat(), which computes the 
              exact probabilities of the Wilcoxon Sign Rank Test Statistic, W.
              The second function, Wilcox.m.test() allows the user to conduct the
              1-Sample Wilcoxon Sign Rank hypothesis test for medians, this also 
              allows the user to conduct the hypothesis test for the normal approximation, 
              based on the techniques of Bickel and Doksum (1973, ISBN:013850363X).
	"""
	
	cran = "wilcoxmed" 

	version("0.0.1", md5="8e508c4904b66791d17269a07d9ecc80")

