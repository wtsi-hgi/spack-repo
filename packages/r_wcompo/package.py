# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWcompo(RPackage):
	"""Semiparametric Proportional Means Regression of Weighted
Composite Endpoint

	Implements inferential and graphic procedures for the semiparametric proportional 
  means regression of weighted composite endpoint of recurrent event and death (Mao and Lin, 
  2016, <doi:10.1093/biostatistics/kxv050>).
	"""
	
	homepage = "https://sites.google.com/view/lmaowisc/"
	cran = "Wcompo" 

	version("1.0", md5="2f57782d3ab726ffbff044f375e44ad6")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
