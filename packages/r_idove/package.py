# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIdove(RPackage):
	"""Durability of Vaccine Efficacy Against SARS-CoV-2 Infection

	Implements a nonparametric maximum likelihood method for assessing 
  potentially time-varying vaccine efficacy (VE) against SARS-CoV-2 infection 
  under staggered enrollment and time-varying community transmission, allowing 
  crossover of placebo volunteers to the vaccine arm. 
  Lin, D. Y., Gu, Y., Zeng, D., Janes, H. E., and Gilbert, P. B. (2021) 
  <doi:10.1093/cid/ciab630>.
	"""
	
	cran = "iDOVE" 

	version("1.5", md5="8e3fbcd236dc6c74fea05c211e13fe90")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
