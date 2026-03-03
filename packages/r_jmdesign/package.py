# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJmdesign(RPackage):
	"""Joint Modeling of Longitudinal and Survival Data - Power
Calculation

	Performs power calculations for joint modeling of longitudinal 
  and survival data with k-th order trajectories when the variance-covariance 
  matrix, Sigma_theta, is unknown.
	"""
	
	cran = "JMdesign" 

	version("1.5", md5="c59bd51aea5366ebb7a7a5807ce40ce7")

