# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMcid(RPackage):
	"""Estimating the Minimal Clinically Important Difference

	Apply the marginal classification method to achieve the purpose of providing 
    the point and interval estimates for the minimal clinically important difference 
    based on the classical anchor-based method. For more details of the methodology, please 
    see Zehua Zhou, Leslie J. Bisson and Jiwei Zhao (2021) <arXiv:2108.11589>.  
	"""
	
	cran = "MCID" 

	version("0.1.0", md5="b0f9bfb2b063c8b8c12be5045f4802f5")

