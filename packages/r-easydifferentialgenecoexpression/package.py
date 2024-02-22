# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasydifferentialgenecoexpression(RPackage):
	"""Easily Performs Differential Coexpression Analysis

	A function that reads in the GEO code of a list of probesets or gene symbols, a gene expression dataset GEO accession code, the name of the dataset feature discriminating the two conditions for the differential coexpression, and the values of the two different conditions for the differential coexpression, and returns the significant pairs of genes/probesets with highest differential coexpression (p-value < 0.005). If the input gene list is made of gene symbols, this package associates the probesets to these gene symbols, if found.  Platforms available: GPL80, GPL8300, GPL80, GPL96, GPL570, GPL571, GPL20115, GPL1293,  GPL6102, GPL6104, GPL6883, GPL6884, GPL13497, GPL14550, GPL17077, GPL6480. GEO: Gene Expression Omnibus. ID: identifier code. The GEO datasets are downloaded from the URL <https://ftp.ncbi.nlm.nih.gov/geo/series/>. 
	"""
	
	homepage = "https://github.com/davidechicco/easyDifferentialGeneCoexpression"
	cran = "easyDifferentialGeneCoexpression" 

	version("1.4", md5="130316c5861349299f2372714414463e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-diffcoexp", type=("build", "run"))
	depends_on("r-geneexpressionfromgeo", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-jetset", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
