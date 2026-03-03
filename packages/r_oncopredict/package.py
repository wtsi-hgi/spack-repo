# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROncopredict(RPackage):
	"""Drug and Biomarker Discovery

	Bridges in vitro drug screening with in vivo drug and biomarker discovery. Specifically, predicts in vivo or cancer patient drug response and biomarkers to enrich for response from cell line screening data. Builds model using ridge regression, and enables biomarker discovery by imputing drug response in large cancer molecular datasets. It also enables drug specific biomarker identification by correcting for general level of drug sensitivity shared among the population. 
	"""
	
	cran = "oncoPredict" 

	version("0.2", md5="a398a44bba1776773fb1fc982551ad41")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-ridge", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-glmnet", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-gdata", type=("build", "run"))
	depends_on("r-tidyverse", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-maftools", type=("build", "run"))
