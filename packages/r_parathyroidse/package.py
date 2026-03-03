# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RParathyroidse(RPackage):
	"""RangedSummarizedExperiment for RNA-Seq of primary cultures of parathyroid tumors by Haglund et al., J Clin Endocrinol Metab 2012.

	This package provides RangedSummarizedExperiment objects of read counts in genes and exonic parts for paired-end RNA-Seq data from experiments on primary cultures of parathyroid tumors.  The data were presented in the article "Evidence of a Functional Estrogen Receptor in Parathyroid Adenomas" by Haglund F, Ma R, Huss M, Sulaiman L, Lu M, Nilsson IL, Hoog A, Juhlin CC, Hartman J, Larsson C, J Clin Endocrinol Metab. jc.2012-2484, Epub 2012 Sep 28, PMID: 23024189.  The sequencing was performed on tumor cultures from 4 patients at 2 time points over 3 conditions (DPN, OHT and control).  One control sample was omitted by the paper authors due to low quality. The package vignette describes the creation of the object from raw sequencing data provided by NCBI Gene Expression Omnibus under accession number GSE37211.  The gene and exon features are the GRCh37 Ensembl annotations.
	"""
	
	bioc = "parathyroidSE" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/parathyroidSE_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/parathyroidSE/parathyroidSE_1.40.0.tar.gz"]

	version("1.40.0", md5="e4d06f888feb4015273e20b14f8ee37a")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

