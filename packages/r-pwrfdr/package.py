# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPwrfdr(RPackage):
	"""FDR Power

	This is a package for calculating two differing notions of power, or deriving sample
 sizes for specified requisite power in multiple testing experiments under a variety of methods for
 control of the distribution of the False Discovery Proportion (FDP). More specifically, one can
 choose to control the FDP distribution according to control of its (i) mean, e.g. the usual BH-FDR
 procedure, or via the probability that it exceeds a given value, delta, via (ii) the Romano
 procedure, or via (iii) my procedure based upon asymptotic approximation. Likewise, we can think of
 the power in multiple testing experiments in terms of a summary of the distribution of the
 True Positive Proportion (TPP). The package will compute power, sample size or any other missing
 parameter required for power based upon (i) the mean of the TPP which is the average power
 (ii) the probability that the TPP exceeds a given value, lambda, via my asymptotic approximation
 procedure. The theoretical results are described in Izmirlian, G. (2020) Stat. and Prob. letters,
 <doi:10.1016/j.spl.2020.108713>, and an applied  paper describing the methodology with a
 simulation study is in preparation.
	"""
	
	cran = "pwrFDR" 

	version("2.8.9", md5="ee53ddb31d7e02898a733e9fd76c829d")

