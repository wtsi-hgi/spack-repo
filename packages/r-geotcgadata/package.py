# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGeotcgadata(RPackage):
	"""Processing Various Types of Data on GEO and TCGA

	Gene Expression Omnibus(GEO) and The Cancer Genome Atlas (TCGA) provide us with a wealth of data, such as RNA-seq, DNA Methylation, SNP and Copy number variation data. It's easy to download data from TCGA using the gdc tool, but processing these data into a format suitable for bioinformatics analysis requires more work. This R package was developed to handle these data.
	"""
	
	homepage = "https://github.com/YuLab-SMU/GeoTcgaData"
	bioc = "GeoTcgaData" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/GeoTcgaData_2.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/GeoTcgaData/GeoTcgaData_2.2.0.tar.gz"]

	version("2.2.0", md5="653a353d37b0bcfbd892dfe12d420100")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cqn", type=("build", "run"))
	depends_on("r-topconfects", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
