# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSamplingr(RPackage):
	"""Sampling and Estimation Methods

	Functions to take samples of data, sample size estimation and getting useful estimators such as total, mean, proportion about its population using simple random, stratified, systematic and cluster sampling. 
	"""
	
	cran = "samplingR" 

	version("1.0.1", md5="9ab0f7933c748b791aa64d8ca233a289")

	depends_on("r-dplyr", type=("build", "run"))
