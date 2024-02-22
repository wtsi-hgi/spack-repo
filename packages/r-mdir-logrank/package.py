# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMdirLogrank(RPackage):
	"""Multiple-Direction Logrank Test

	Implemented are the one-sided and two-sided 
  multiple-direction logrank test for two-sample right 
  censored data. In addition to the statistics p-values are calculated: 
  1. For the one-sided testing problem one p-value based on a
   wild bootstrap approach is determined. 2. In the two-sided case
   one p-value based on a chi-squared approximation and 
   a second p-values based on a permutation approach are calculated.
 Ditzhaus, M. and Friedrich, S. (2018) <arXiv:1807.05504>.
 Ditzhaus, M. and Pauly, M. (2018) <arXiv:1808.05627>.
	"""
	
	cran = "mdir.logrank" 

	version("0.0.4", md5="07aec0abb97f398ece9b794be8207dd9")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-mass@7.3.47:", type=("build", "run"))
