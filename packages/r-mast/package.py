# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
	
from spack.package import *
	
			
class RMast(RPackage):
	"""Model-based Analysis of Single Cell Transcriptomics

	Methods and models for handling zero-inflated single cell assay data.
	"""
	
	homepage = "https://github.com/RGLab/MAST/"
	bioc = "MAST" 

	version("1.28.0", commit="2a0af38010795d6210c40892e4ff43e8838bfcab")

	depends_on("r-singlecellexperiment@1.2.0:", type=("build", "run"))
	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.5.3:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
