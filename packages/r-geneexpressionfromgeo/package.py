# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeneexpressionfromgeo(RPackage):
	"""Easily Downloads a Gene Expression Dataset from a GEO Code and
Retrieves the Gene Symbols of Its Probesets

	A function that reads in the GEO code of a gene expression dataset, retrieves its data from GEO, (optionally) retrieves the gene symbols of the dataset, and returns a simple dataframe table containing all the data. Platforms available: GPL11532, GPL23126, GPL6244, GPL8300, GPL80, GPL96, GPL570, GPL571, GPL20115, GPL1293,  GPL6102, GPL6104, GPL6883, GPL6884, GPL13497, GPL14550, GPL17077, GPL6480. GEO: Gene Expression Omnibus. ID: identifier code. The GEO datasets are downloaded from the URL <https://ftp.ncbi.nlm.nih.gov/geo/series/>. More information can be found in the following manuscript: Davide Chicco, "geneExpressionFromGEO: an R package to facilitate data reading from Gene Expression Omnibus (GEO)". Microarray Data Analysis, Methods in Molecular Biology, volume 2401, chapter 12, pages 187-194, Springer Protocols, 2021, <doi:10.1007/978-1-0716-1839-4_12>.
	"""
	
	homepage = "https://github.com/davidechicco/geneExpressionFromGEO"
	cran = "geneExpressionFromGEO" 

	version("0.9", md5="0841b94b0eccdc4c31d1232e06291154")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-biocmanager", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
