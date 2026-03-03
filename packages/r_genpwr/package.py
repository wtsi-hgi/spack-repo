# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenpwr(RPackage):
	"""Power Calculations Under Genetic Model Misspecification

	Power and sample size calculations for genetic association studies allowing 
    for misspecification of the model of genetic susceptibility.
    "Hum Hered. 2019;84(6):256-271.<doi:10.1159/000508558>. Epub 2020 Jul 28."
    Power and/or sample size can be calculated for logistic (case/control study design) 
    and linear (continuous phenotype) regression models, using additive, dominant, 
    recessive or degree of freedom coding of the genetic covariate while assuming 
    a true dominant, recessive or additive genetic effect. In addition, power and 
    sample size calculations can be performed for gene by environment interactions.  
    These methods are extensions of Gauderman (2002) 
    <doi:10.1093/aje/155.5.478> and Gauderman (2002) <doi:10.1002/sim.973>
    and are described in: 
    Moore CM, Jacobson S, Fingerlin TE. Power and Sample Size Calculations 
    for Genetic Association Studies in the Presence of Genetic Model Misspecification. 
    American Society of Human Genetics. 
    October 2018, San Diego. 
	"""
	
	cran = "genpwr" 

	version("1.0.4", md5="88ac7b91157851edf81a1bcfec6556a8")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nleqslv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
