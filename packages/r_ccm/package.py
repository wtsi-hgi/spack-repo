# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCcm(RPackage):
	"""Correlation Classification Method

	Classification method described in Dancik et al (2011) <doi:10.1158/0008-5472.CAN-11-2427> that classifies a sample according to the class with the maximum mean (or any other function of) correlation between the test and training samples with known classes.
	"""
	
	cran = "CCM" 

	version("1.2", md5="216dcdb72ed6ccf6db3082d9cd2cc7d6")

