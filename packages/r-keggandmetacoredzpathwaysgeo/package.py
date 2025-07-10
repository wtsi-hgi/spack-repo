# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeggandmetacoredzpathwaysgeo(RPackage):
	"""Disease Datasets from GEO

	This is a collection of 18 data sets for which the phenotype is a disease with a corresponding pathway in either KEGG or metacore database.This collection of datasets were used as gold standard in comparing gene set analysis methods.
	"""
	
	bioc = "KEGGandMetacoreDzPathwaysGEO" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/KEGGandMetacoreDzPathwaysGEO_1.22.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/KEGGandMetacoreDzPathwaysGEO/KEGGandMetacoreDzPathwaysGEO_1.22.0.tar.gz"]

	version("1.22.0", sha256="7ae2c43cbd4add25c2003946c819f391a11ce8bd16a0d68a8e88915bfa2fb6e6")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

