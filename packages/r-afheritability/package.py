# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAfheritability(RPackage):
	"""The Attributable Fraction (AF) Described as a Function of
Disease Heritability, Prevalence and Intervention Specific
Factors

	The AFfunction() is a function which returns an estimate of the Attributable Fraction (AF) and a plot of the AF as a function of heritability, disease prevalence, size of target group and intervention effect. 
             Since the AF is a function of several factors, a shiny app is used to better illustrate how the relationship between the AF and heritability depends on several other factors. The app is ran by the function runShinyApp().
             For more information see Dahlqwist E et al. (2019) <doi:10.1007/s00439-019-02006-8>.
	"""
	
	cran = "AFheritability" 

	version("0.1.0", md5="62c5894417a6e6995124306b4dbaed86")

	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
