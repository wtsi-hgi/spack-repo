# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDistdichor(RPackage):
	"""Distributional Method for the Dichotomisation of Continuous
Outcomes

	Contains a range of functions covering the present
  development of the distributional method for the dichotomisation of continuous outcomes. 
  The method provides estimates with standard error of a comparison of proportions 
  (difference, odds ratio and risk ratio) derived, with similar precision, from a comparison of means. 
  See the URL below or <arXiv:1809.03279> for more information.
	"""
	
	homepage = "https://arxiv.org/abs/1809.03279"
	cran = "distdichoR" 

	version("0.1-1", md5="785a483f9056b00a46dca200449f2fbc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-sn", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
