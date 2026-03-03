# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmzqc(RPackage):
	"""Creation, Reading and Validation of 'mzqc' Files

	Reads, writes and validates 'mzQC' files. The 'mzQC' format is a 
  standardized file format for the exchange, transmission, and archiving of 
  quality metrics derived from biological mass spectrometry data, as defined 
  by the HUPO-PSI (Human Proteome Organisation - Proteomics Standards Initiative) 
  Quality Control working group. 
  See <https://hupo-psi.github.io/mzQC/> for details.
	"""
	
	homepage = "https://github.com/MS-Quality-hub/rmzqc"
	cran = "rmzqc" 

	version("0.5.3", md5="59234a876928a14bad060c8dcb346284")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jsonvalidate", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-ontologyindex", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-r6p", type=("build", "run"))
	depends_on("r-testthat", type=("build", "run"))
