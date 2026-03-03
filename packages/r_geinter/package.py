# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeinter(RPackage):
	"""Robust Gene-Environment Interaction Analysis

	Description: For the risk, progression, and response to treatment of many complex diseases, it has been increasingly recognized that gene-environment interactions play important roles beyond the main genetic and environmental effects. In practical interaction analyses, outliers in response variables and covariates are not uncommon. In addition, missingness in environmental factors is routinely encountered in epidemiological studies. The developed package consists of five robust approaches to address the outliers problems, among which two approaches can also accommodate missingness in environmental factors. Both continuous and right censored responses are considered. The proposed approaches are based on penalization and sparse boosting techniques for identifying important interactions, which are realized using efficient algorithms. Beyond the gene-environment analysis, the developed package can also be adopted to conduct analysis on interactions between other types of low-dimensional and high-dimensional data. (Mengyun Wu et al (2017), <doi:10.1080/00949655.2018.1523411>; Mengyun Wu et al (2017), <doi:10.1002/gepi.22055>; Yaqing Xu et al (2018), <doi:10.1080/00949655.2018.1523411>; Yaqing Xu et al (2019), <doi:10.1016/j.ygeno.2018.07.006>; Mengyun Wu et al (2021), <doi:10.1093/bioinformatics/btab318>). 
	"""
	
	cran = "GEInter" 

	version("0.3.2", md5="dfa4c3addadb5ecc7662b0d3d6583ca1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-pcapp", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
