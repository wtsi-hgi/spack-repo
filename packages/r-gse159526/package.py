# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGse159526(RPackage):
	"""Placental cell DNA methylation data from GEO accession GSE159526

	19 term and 9 first trimester placental chorionic villi and matched cell-sorted samples ran on Illumina HumanMethylationEPIC DNA methylation microarrays. This data was made available on GEO accession [GSE159526](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE159526). Both the raw and processed data has been made available on code{ExperimentHub}. Raw unprocessed data formatted as an RGChannelSet object for integration and normalization using minfi and other existing Bioconductor packages. Processed normalized data is also available as a DNA methylation code{matrix}, with a corresponding phenotype information as a code{data.frame} object.
	"""
	
	homepage = "https://github.com/wvictor14/GSE159526"
	bioc = "GSE159526" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/GSE159526_1.8.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/GSE159526/GSE159526_1.8.0.tar.gz"]

	version("1.8.0", md5="d89442c94cb87f0760a9f0f85426a8fa", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/GSE159526_1.8.0.tar.gz")


	# experiment