# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBcra(RPackage):
	"""Breast Cancer Risk Assessment

	Functions provide risk projections of invasive breast cancer based on Gail model according to National Cancer Institute's Breast Cancer Risk Assessment Tool algorithm for specified race/ethnic groups and age intervals.
             Gail MH, Brinton LA, et al (1989) <doi:10.1093/jnci/81.24.1879>. 
             Marthew PB, Gail MH, et al (2016) <doi:10.1093/jnci/djw215>.
	"""
	
	cran = "BCRA" 

	version("2.1.2", md5="2850d31820ed691b513fadf763fa34da")

