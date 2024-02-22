# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenehummus(RPackage):
	"""A Pipeline to Define Gene Families in Legumes and Beyond

	A pipeline with high specificity and sensitivity in extracting 
  proteins from the RefSeq database (National Center for Biotechnology 
  Information). Manual identification of gene families is highly 
  time-consuming and laborious, requiring an iterative process of manual and 
  computational analysis to identify members of a given family. The pipelines 
  implements an automatic approach for the identification of gene families 
  based on the conserved domains that specifically define that family. See 
  Die et al. (2018) <doi:10.1101/436659> for more information and examples.
	"""
	
	homepage = "https://github.com/NCBI-Hackathons/GeneHummus"
	cran = "geneHummus" 

	version("1.0.11", md5="72bdf2c73f9a03f2ce398b8198831bcc")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rentrez@1.2.1:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-dplyr@0.8.0.1:", type=("build", "run"))
	depends_on("r-httr@1.4:", type=("build", "run"))
	depends_on("r-curl@3.3:", type=("build", "run"))
