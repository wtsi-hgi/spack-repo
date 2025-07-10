# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBgeedb(RPackage):
	"""Annotation and gene expression data retrieval from Bgee database. TopAnat, an anatomical entities Enrichment Analysis tool for UBERON ontology

	A package for the annotation and gene expression data download from Bgee database, and TopAnat analysis: GO-like enrichment of anatomical terms, mapped to genes by expression patterns.
	"""
	
	homepage = "https://github.com/BgeeDB/BgeeDB_R"
	bioc = "BgeeDB" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/BgeeDB_2.28.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/BgeeDB/BgeeDB_2.28.0.tar.gz"]

	version("2.28.0", sha256="d6e62249a3d00f6f288ea6ddf4e1100433d1be67417980a14f8fc3c883b811aa")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
