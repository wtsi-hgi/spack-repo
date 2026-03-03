# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReappraised(RPackage):
	"""Statistical Tools for Assessing Publication Integrity of Groups
of Trials

	Takes user-provided baseline data from groups of randomised controlled data and  
    assesses whether the observed distribution of baseline p-values, numbers of participants 
    in each group, or categorical variables are consistent with the expected distribution, as 
    an aid to the assessment of integrity concerns in published randomised controlled trials. 
    References (citations in PubMed format in details of each function):
    Bolland MJ, Avenell A, Gamble GD, Grey A. (2016) <doi:10.1212/WNL.0000000000003387>.
    Bolland MJ, Gamble GD, Avenell A, Grey A, Lumley T. (2019) 
    <doi:10.1016/j.jclinepi.2019.05.006>.
    Bolland MJ, Gamble GD, Avenell A, Grey A. (2019) <doi:10.1016/j.jclinepi.2019.03.001>.
    Bolland MJ, Gamble GD, Grey A, Avenell A. (2020) <doi:10.1111/anae.15165>.
    Bolland MJ, Gamble GD, Avenell A, Cooper DJ, Grey A. (2021) 
    <doi:10.1016/j.jclinepi.2020.11.012>.
    Bolland MJ, Gamble GD, Avenell A, Grey A. (2021) <doi:10.1016/j.jclinepi.2021.05.002>.
    Bolland MJ, Gamble GD, Avenell A, Cooper DJ, Grey A. (2023) 
    <doi:10.1016/j.jclinepi.2022.12.018>.
    Carlisle JB, Loadsman JA. (2017) <doi:10.1111/anae.13650>.
    Carlisle JB. (2017) <doi:10.1111/anae.13938>.
	"""
	
	cran = "reappraised" 

	version("0.1.1", md5="d8487d9ae121311360ec16bd29a3376d")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-broom", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-epitools", type=("build", "run"))
	depends_on("r-flextable", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggpubr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-vcd", type=("build", "run"))
	depends_on("r-vcdextra", type=("build", "run"))
