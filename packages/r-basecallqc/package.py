# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBasecallqc(RPackage):
	"""Working with Illumina Basecalling and Demultiplexing input and output files

	The basecallQC package provides tools to work with Illumina bcl2Fastq (versions >= 2.1.7) software.Prior to basecalling and demultiplexing using the bcl2Fastq software, basecallQC functions allow the user to update Illumina sample sheets from versions <= 1.8.9 to >= 2.1.7 standards, clean sample sheets of common problems such as invalid sample names and IDs, create read and index basemasks and the bcl2Fastq command. Following the generation of basecalled and demultiplexed data, the basecallQC packages allows the user to generate HTML tables, plots and a self contained report of summary metrics from Illumina XML output files.
	"""
	
	bioc = "basecallQC" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/basecallQC_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/basecallQC/basecallQC_1.26.0.tar.gz"]

	version("1.26.0", md5="ad61b901f8e533f817dccfb4830b222a")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-prettydoc", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-raster", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-lazyeval", type=("build", "run"))
	depends_on("r-shortread", type=("build", "run"))
