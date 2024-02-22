# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTransmodel(RPackage):
	"""Fit Linear Transformation Models for Right Censored Data

	A unified estimation procedure for the analysis of right censored data using linear transformation models. An introduction can be found in Jie Zhou et al. (2022) <doi:10.18637/jss.v101.i09>. 
	"""
	
	cran = "TransModel" 

	version("2.3", md5="39705daacc0d1ef4521f9b93f74c333a")

	depends_on("r-survival", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
