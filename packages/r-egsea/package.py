# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REgsea(RPackage):
	"""Ensemble of Gene Set Enrichment Analyses

	This package implements the Ensemble of Gene Set Enrichment Analyses (EGSEA) method for gene set testing. EGSEA algorithm utilizes the analysis results of twelve prominent GSE algorithms in the literature to calculate collective significance scores for each gene set.
	"""
	
	bioc = "EGSEA" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/EGSEA_1.30.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/EGSEA/EGSEA_1.30.1.tar.gz"]

	version("1.30.1", md5="6df5ddde1ce67014d637e6196177c11b")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-gage@2.14.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-topgo@2.16:", type=("build", "run"))
	depends_on("r-pathview@1.4.2:", type=("build", "run"))
	depends_on("r-padog@1.6:", type=("build", "run"))
	depends_on("r-gsva@1.12:", type=("build", "run"))
	depends_on("r-globaltest@5.18:", type=("build", "run"))
	depends_on("r-limma@3.20.9:", type=("build", "run"))
	depends_on("r-edger@3.6.8:", type=("build", "run"))
	depends_on("r-htmlutils@0.1.5:", type=("build", "run"))
	depends_on("r-hwriter@1.2.2:", type=("build", "run"))
	depends_on("r-gplots@2.14.2:", type=("build", "run"))
	depends_on("r-ggplot2@1:", type=("build", "run"))
	depends_on("r-safe@3.4:", type=("build", "run"))
	depends_on("r-stringi@0.5:", type=("build", "run"))
	depends_on("r-metap", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-org-rn-eg-db", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-egseadata@1.3.1:", type=("build", "run"))
	depends_on("r-htmlwidgets", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
