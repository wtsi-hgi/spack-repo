# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWyzCodeOffensiveprogramming(RPackage):
	"""Wizardry Code Offensive Programming

	Allows to turn standard R code into offensive programming code. 
    Provides code instrumentation to ease this change and tools to assist and 
    accelerate code production and tuning while using offensive programming code 
    technics. 
    Should improve code robustness and quality. Function calls can be easily 
    verified on-demand or in batch mode to assess parameter types and length 
    conformities. 
    Should improve coders productivity as offensive programming reduces the code
    size due to reduced number of controls all along the call chain. 
    Should speed up processing as many checks will be reduced to one single check.
	"""
	
	homepage = "https://neonira.github.io/offensiveProgrammingBook_v1.2.2/"
	cran = "wyz.code.offensiveProgramming" 

	version("1.1.24", md5="585d388c257ac73b889300558227fd58")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-r6@2.4:", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
