# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpmlda(RPackage):
	"""Nonparametric Models for Longitudinal Data

	Support the book: Wu CO and Tian X (2018). Nonparametric Models for Longitudinal Data. 
             Chapman & Hall/CRC (to appear); and provide fit for using global and local smoothing methods
             for the conditional-mean and conditional-distribution based models with longitudinal Data.
	"""
	
	homepage = "https://github.com/npmldabook/npmlda/"
	cran = "npmlda" 

	version("1.0.0", md5="6dfab940f4349efa7269536469c2da39")

	depends_on("r@3:", type=("build", "run"))
