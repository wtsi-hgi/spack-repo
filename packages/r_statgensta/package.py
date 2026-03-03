# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatgensta(RPackage):
	"""Single Trial Analysis (STA) of Field Trials

	Phenotypic analysis of field trials using mixed models with and 
    without spatial components. One of a series of statistical genetic packages 
    for streamlining the analysis of typical plant breeding experiments developed
    by Biometris.    
    Some functions have been created to be used in conjunction with the R 
    package 'asreml' for the 'ASReml' software, which can be obtained upon 
    purchase from 'VSN' international (<https://vsni.co.uk/software/asreml-r>). 
	"""
	
	homepage = "https://biometris.github.io/statgenSTA/index.html"
	cran = "statgenSTA" 

	version("1.0.12", md5="2a569561c71e99b4608649e7aee76716")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-emmeans", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-mapproj", type=("build", "run"))
	depends_on("r-maps", type=("build", "run"))
	depends_on("r-qtl", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-scales@1.1:", type=("build", "run"))
	depends_on("r-spats@1.0.18:", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
