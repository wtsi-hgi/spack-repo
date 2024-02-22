# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVacuum(RPackage):
	"""Tukey's Vacuum Cleaner

	An implementation of three procedures developed by 
    John Tukey: FUNOP (FUll NOrmal Plot), FUNOR-FUNOM 
    (FUll NOrmal Rejection-FUll NOrmal Modification), and vacuum cleaner. 
    Combined, they provide a way to identify, treat, and analyze outliers 
    in two-way (i.e., contingency) tables, as described in his 
    landmark paper "The Future of Data Analysis", Tukey, John W. (1962) 
    <https://www.jstor.org/stable/2237638>. 
	"""
	
	homepage = "https://github.com/Sielinski/vacuum"
	cran = "vacuum" 

	version("0.1.0", md5="2166479d4dee1baba23549ab65ee7778")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
