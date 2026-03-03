# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobvis(RPackage):
	"""Visualize the Results of Risk-of-Bias (ROB) Assessments

	Helps users in quickly visualizing risk-of-bias 
    assessments performed as part of a systematic review. It allows users to 
    create weighted bar-plots of the distribution of risk-of-bias judgments 
    within each bias domain, in addition to traffic-light plots of the 
    specific domain-level judgments for each study. The resulting figures are 
    of publication quality and are formatted according the risk-of-bias 
    assessment tool use to perform the assessments. Currently, the supported 
    tools are ROB2.0 (for randomized controlled trials; Sterne et al (2019)  
    <doi:10.1136/bmj.l4898>), ROBINS-I (for non-randomised studies of 
    interventions; Sterne et al (2016) <doi:10.1136/bmj.i4919>), and QUADAS-2 
    (for diagnostic accuracy studies; Whiting et al (2011) 
    <doi:10.7326/0003-4819-155-8-201110180-00009>).
	"""
	
	homepage = "https://github.com/mcguinlu/robvis"
	cran = "robvis" 

	version("0.3.0", md5="64befbef23fe9d82ba1d3d4bb1cb9c65")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
