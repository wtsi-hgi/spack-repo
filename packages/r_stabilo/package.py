# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStabilo(RPackage):
	"""Stabilometric Signal Quantification

	
    Functions for stabilometric signal quantification.      
    The input is a data frame containing the x, y coordinates of the center-of-pressure displacement.     
    Jose Magalhaes de Oliveira (2017) <doi:10.3758/s13428-016-0706-4> "Statokinesigram normalization method";       
    T E Prieto, J B Myklebust, R G Hoffmann, E G Lovett, B M Myklebust (1996) <doi:10.1109/10.532130> "Measures of postural steadiness: Differences between healthy young and elderly adults";      
    L F Oliveira et al (1996) <doi:10.1088/0967-3334/17/4/008> "Calculation of area of stabilometric signals using principal component analisys".
	"""
	
	cran = "stabilo" 

	version("0.1.1", md5="049d2ce37e3bc48fcfd39118f32f74fd")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
