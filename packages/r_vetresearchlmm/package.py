# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVetresearchlmm(RPackage):
	"""Linear Mixed Models - An Introduction with Applications in
Veterinary Research

	R Codes and Datasets for Duchateau, L. and Janssen, P. and Rowlands, G. J. (1998). Linear Mixed Models. An Introduction with applications in Veterinary Research. International Livestock Research Institute.
	"""
	
	homepage = "https://github.com/MYaseen208/VetResearchLMM"
	cran = "VetResearchLMM" 

	version("1.0.0", md5="367b7253932e491239a7276ceedef2b6")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-multcomp", type=("build", "run"))
