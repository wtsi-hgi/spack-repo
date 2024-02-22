# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDrawsample(RPackage):
	"""Draw Samples with the Desired Properties from a Data Set

	A tool to sample data with the desired properties.Samples can be 
    drawn by purposive sampling with determining distributional 
    conditions, such as deviation from normality (skewness and kurtosis), 
    and sample size in quantitative research studies.
    For purposive sampling, a researcher has something in mind and participants that 
    fit the purpose of the study are included (Etikan,Musa, & Alkassim, 2015) 
    <doi:10.11648/j.ajtas.20160501.11>.Purposive sampling can be useful for answering
    many research questions (Klar & Leeper, 2019) 
    <doi:10.1002/9781119083771.ch21>.
	"""
	
	homepage = "https://github.com/atalay-k/drawsample"
	cran = "drawsample" 

	version("1.0.1", md5="9c606236ebd182e96fc62562720e1e09")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-psych", type=("build", "run"))
	depends_on("r-moments", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinycssloaders", type=("build", "run"))
	depends_on("r-shinydashboard", type=("build", "run"))
	depends_on("r-xlsx", type=("build", "run"))
