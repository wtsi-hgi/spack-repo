# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKeggdzpathwaysgeo(RPackage):
	"""KEGG Disease Datasets from GEO

	This is a collection of 24 data sets for which the phenotype is a disease with a corresponding pathway in the KEGG database.This collection of datasets were used as gold standard in comparing gene set analysis methods by the PADOG package.
	"""
	
	bioc = "KEGGdzPathwaysGEO" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/KEGGdzPathwaysGEO_1.40.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/KEGGdzPathwaysGEO/KEGGdzPathwaysGEO_1.40.0.tar.gz"]

	version("1.40.0", md5="2f30f9ac05c04214d25a9d49fb4ce8bd")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))

	# experiment