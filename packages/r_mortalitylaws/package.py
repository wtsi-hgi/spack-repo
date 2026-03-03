# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMortalitylaws(RPackage):
	"""Parametric Mortality Models, Life Tables and HMD

	Fit the most popular human mortality 'laws', and construct 
  full and abridge life tables given various input indices. A mortality
  law is a parametric function that describes the dying-out process of 
  individuals in a population during a significant portion of their 
  life spans. For a comprehensive review of the most important mortality 
  laws see Tabeau (2001) <doi:10.1007/0-306-47562-6_1>. 
  Practical functions for downloading data from various human mortality 
  databases are provided as well.  
	"""
	
	homepage = "https://github.com/mpascariu/MortalityLaws"
	cran = "MortalityLaws" 

	version("2.1.0", md5="a4d3efdc1d5a22827790a52ad348303b")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-minpack-lm@1.2:", type=("build", "run"))
	depends_on("r-rcurl@1.95:", type=("build", "run"))
	depends_on("r-pbapply@1.3.4:", type=("build", "run"))
	depends_on("r-tidyr@0.8.1:", type=("build", "run"))
	depends_on("r-rvest@1.0.3:", type=("build", "run"))
	depends_on("r-httr@1.4.5:", type=("build", "run"))
