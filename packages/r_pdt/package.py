# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdt(RPackage):
	"""Permutation Distancing Test

	Permutation (randomisation) test for single-case phase design data with 
    two phases (e.g., pre- and post-treatment). Correction for dependency of observations 
    is done through stepwise resampling the time series while varying 
    the distance between observations. The required distance 0,1,2,3.. is determined 
    based on repeated dependency testing while stepwise increasing the distance.
    In preparation: Vroegindeweij et al. "A Permutation distancing test 
    for single-case observational AB phase design data: A Monte Carlo simulation study".
	"""
	
	cran = "pdt" 

	version("0.0.2", md5="51d57ed5f397aeae1bd72510816d57a8")

	depends_on("r@4.1:", type=("build", "run"))
