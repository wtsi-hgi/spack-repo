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

	version("0.4.0", md5="89800fb63ee455786036bb5652070ea6")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
