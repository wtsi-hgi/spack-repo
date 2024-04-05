# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgengxe(RPackage):
	"""Genotype by Environment (GxE) Analysis

	Analysis of multi environment data of plant breeding experiments
    following the analyses described in Malosetti, Ribaut, 
    and van Eeuwijk (2013), <doi:10.3389/fphys.2013.00044>.
    One of a series of statistical genetic packages for streamlining the analysis of 
    typical plant breeding experiments developed by Biometris.
    Some functions have been created to be used in conjunction with the R 
    package 'asreml' for the 'ASReml' software, which can be obtained upon 
    purchase from 'VSN' international (<https://vsni.co.uk/software/asreml-r>).
	"""
	
	homepage = "https://biometris.github.io/statgenGxE/index.html"
	cran = "statgenGxE" 

	version("1.0.7", md5="50af32e6e5e1bc54ed9b460fa616015a")
	version("1.0.6", md5="3146aaf9e87e377b38ce69d5d2b03c6b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-statgensta@1.0.6:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
