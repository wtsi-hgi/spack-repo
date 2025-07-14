# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSingleMtecTranscriptomes(RPackage):
	"""Single Cell Transcriptome Data and Analysis of Mouse mTEC cells

	This data package contains the code used to analyse the single-cell RNA-seq and the bulk ATAC-seq data from the manuscript titled: Single-cell transcriptome analysis reveals coordinated ectopic-gene expression patterns in medullary thymic epithelial cells. This paper was published in Nature Immunology 16,933-941(2015). The data objects provided in this package has been pre-processed: the raw data files can be downloaded from ArrayExpress under the accession identifiers E-MTAB-3346 and E-MTAB-3624. The vignette of this data package provides a documented and reproducible workflow that includes the code that was used to generate each statistic and figure from the manuscript.
	"""
	
	bioc = "Single.mTEC.Transcriptomes" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Single.mTEC.Transcriptomes_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/Single.mTEC.Transcriptomes/Single.mTEC.Transcriptomes_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="6a739151d4b5d4993ed75f88fa03f11656a1f17e0745ad34959a1cec6a386ef0")

	depends_on("r@3.5:", type=("build", "run"))

