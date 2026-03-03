# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFunta(RPackage):
	"""Functional Tangential Angle Pseudo-Depth

	Computes the functional tangential angle pseudo-depth and its robustified version from the paper by Kuhnt and Rehage (2016). See Kuhnt, S.; Rehage, A. (2016): An angle-based multivariate functional pseudo-depth for shape outlier detection, JMVA 146, 325-340, <doi:10.1016/j.jmva.2015.10.016> for details. 
	"""
	
	cran = "FUNTA" 

	version("0.1.0", md5="3ed4abcc2c1706d0a9cfa58c614d58ba")

