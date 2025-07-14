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

	version("1.36.0", commit="a8ea38726cc575afb4160c30ae9f138801ad45bc")
	version("1.30.0", commit="97cfae591fe6fc4cd80c7c06b8415358ffc38236")

	depends_on("r@3.5:", type=("build", "run"))

