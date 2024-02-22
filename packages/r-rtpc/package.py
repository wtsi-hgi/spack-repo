# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtpc(RPackage):
	"""Fitting and Analysing Thermal Performance Curves

	Helps to fit thermal performance curves (TPCs). 'rTPC' contains 26 model formulations previously used to fit TPCs and has helper functions to set sensible start parameters, upper and lower parameter limits and estimate parameters useful in downstream analyses, such as cardinal temperatures, maximum rate and optimum temperature. See Padfield et al. (2021) <doi:10.1111/2041-210X.13585>.
	"""
	
	homepage = "https://github.com/padpadpadpad/rTPC"
	cran = "rTPC" 

	version("1.0.4", md5="14fda948a29e922a7bbe2aba3d8df0a4")

	depends_on("r@2.10:", type=("build", "run"))
