# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RTtservice(RPackage):
	"""A Service for Tidy Transcriptomics Software Suite

	It provides generic methods that are used by more than one package, avoiding conflicts. This package will be imported by 'tidySingleCellExperiment' and 'tidyseurat'. 
	"""
	
	cran = "ttservice" 

	version("0.3.8", md5="80e5ea9851569e9905adbbff1ce7a6a2")

	depends_on("r@4.0.0:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))

