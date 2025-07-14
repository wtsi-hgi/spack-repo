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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GeoTcgaData_2.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GeoTcgaData/GeoTcgaData_2.2.0.tar.gz"]

	version("2.8.0", tag="RELEASE_3_21")
	version("2.2.0", sha256="077c28251e23d51c4471b9259dd1246bb26dbaccb3249a67e31356311c8a8bd6")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-cqn", type=("build", "run"))
	depends_on("r-topconfects", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
