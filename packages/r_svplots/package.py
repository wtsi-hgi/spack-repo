# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvplots(RPackage):
	"""Sample Variance Plots (Sv-Plots)

	Two versions of sample variance plots, Sv-plot1 and Sv-plot2, will be provided illustrating 
             the squared deviations from sample variance. Besides indicating the contribution of squared 
             deviations for the sample variability, these plots are capable of detecting characteristics of the
             distribution such as symmetry, skewness and outliers. A remarkable graphical method based on 
             Sv-plot2 can determine the decision on testing hypotheses over one or two population means. 
             In sum, Sv-plots will be appealing visualization tools. Complete description of this methodology  
             can be found in the article, Wijesuriya (2020) <doi:10.1080/03610918.2020.1851716>. 
	"""
	
	cran = "svplots" 

	version("0.1.0", md5="47c0d20b6e0b37b0d65f4d52175ac153")

	depends_on("r@3.0.2:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
