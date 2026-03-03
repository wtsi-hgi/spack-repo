# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGrplasso(RPackage):
	"""Fitting User-Specified Models with Group Lasso Penalty

	Fits user-specified (GLM-) models with group lasso penalty.
	"""
	
	cran = "grplasso" 

	version("0.4-7", md5="7ab430cab104114dc292f217fbc6eddc")

