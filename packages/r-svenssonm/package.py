# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvenssonm(RPackage):
	"""Svensson's Method

	Obtain parameters of Svensson's Method, including percentage agreement, 
    systematic change and individual change. Also, the contingency table can be generated. 
    Svensson's Method is a rank-invariant nonparametric method for the analysis of ordered scales 
    which measures the level of change both from systematic and individual aspects. For the details, 
    please refer to Svensson E. Analysis of systematic and random differences between paired ordinal 
    categorical data [dissertation]. Stockholm: Almqvist & Wiksell International; 1993.
	"""
	
	cran = "svenssonm" 

	version("0.1.0", md5="37ea6932a13f25448d1a2256479c8331")

