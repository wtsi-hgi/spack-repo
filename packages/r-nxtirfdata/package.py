# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNxtirfdata(RPackage):
	"""Data for NxtIRF

	NxtIRFdata is a companion package for SpliceWiz, an interactive analysis and visualization tool for alternative splicing quantitation (including intron retention) for RNA-seq BAM files. NxtIRFdata contains Mappability files required for the generation of human and mouse references. NxtIRFdata also contains a synthetic genome reference and example BAM files used to demonstrate SpliceWiz's functionality. BAM files are based on 6 samples from the Leucegene dataset provided by NCBI Gene Expression Omnibus under accession number GSE67039.
	"""
	
	homepage = "https://github.com/alexchwong/NxtIRFdata"
	bioc = "NxtIRFdata" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/NxtIRFdata_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/NxtIRFdata/NxtIRFdata_1.8.0.tar.gz"]

	version("1.8.0", md5="3d9c35f12650fe6e2eb413224b3590dc")

	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))

	# experiment