# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrsra(RPackage):
	"""Tidying and Analyzing 'Coursera' Research Export Data

	Tidies and performs preliminary analysis of 'Coursera' research
    export data. These export data can be downloaded by anyone who has classes
    on Coursera and wants to analyze the data. Coursera is one of the leading 
    providers of MOOCs and was launched in January 2012. With over 25 million 
    learners, Coursera is the most popular provider in the world being followed 
    by EdX, the MOOC provider that was a result of a collaboration between 
    Harvard University and MIT, with over 10 million users. Coursera has over 
    150 university partners from 29 countries and offers a total of 2000+ 
    courses from computer science to philosophy. Besides, Coursera offers 180+ 
    specialization, Coursera's credential system, and four fully online Masters 
    degrees. For more information about Coursera check Coursera's
    About page on <https://blog.coursera.org/about/>.
	"""
	
	cran = "crsra" 

	version("0.2.3", md5="89ef89d66a0f1adf6bc31433d4df2a21")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-tidytext", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rcorpora", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
