# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSvmdo(RPackage):
	"""Identification of Tumor-Discriminating mRNA Signatures via Support Vector Machines Supported by Disease Ontology

	It is an easy-to-use GUI using disease information for detecting tumor/normal sample discriminating gene sets from differentially expressed genes. Our approach is based on an iterative algorithm filtering genes with disease ontology enrichment analysis and wilk and wilk’s lambda criterion connected to SVM classification model construction. Along with gene set extraction, SVMDO also provides individual prognostic marker detection. The algorithm is designed for FPKM and RPKM normalized RNA-Seq transcriptome datasets.
	"""
	
	bioc = "SVMDO" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SVMDO_1.2.8.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SVMDO/SVMDO_1.2.8.tar.gz"]

	version("1.2.8", sha256="128e27afa062cd585b4cac2438c490c63d232806ea35462696b327130169e2de")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-shiny@1.7.4:", type=("build", "run"))
	depends_on("r-shinyfiles@0.9.3:", type=("build", "run"))
	depends_on("r-shinytitle@0.1:", type=("build", "run"))
	depends_on("r-golem@0.3.5:", type=("build", "run"))
	depends_on("r-nortest@1.0.4:", type=("build", "run"))
	depends_on("r-e1071@1.7.12:", type=("build", "run"))
	depends_on("r-bsda@1.2.1:", type=("build", "run"))
	depends_on("r-data-table@1.14.6:", type=("build", "run"))
	depends_on("r-sjmisc@2.8.9:", type=("build", "run"))
	depends_on("r-klar@1.7.1:", type=("build", "run"))
	depends_on("r-catools@1.18.2:", type=("build", "run"))
	depends_on("r-caret@6.0.93:", type=("build", "run"))
	depends_on("r-survival@3.4.0:", type=("build", "run"))
	depends_on("r-dose@3.24.2:", type=("build", "run"))
	depends_on("r-annotationdbi@1.60:", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.16:", type=("build", "run"))
	depends_on("r-dplyr@1.0.10:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.28:", type=("build", "run"))
