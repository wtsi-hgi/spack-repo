# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmplican(RPackage):
	"""Automated analysis of CRISPR experiments

	`amplican` performs alignment of the amplicon reads, normalizes gathered data, calculates multiple statistics (e.g. cut rates, frameshifts) and presents results in form of aggregated reports. Data and statistics can be broken down by experiments, barcodes, user defined groups, guides and amplicons allowing for quick identification of potential problems.
	"""
	
	homepage = "https://github.com/valenlab/amplican"
	bioc = "amplican" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/amplican_1.24.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/amplican/amplican_1.24.0.tar.gz"]

	version("1.30.0", tag="RELEASE_3_21")
	version("1.24.0", sha256="9c6a1fd6d0016b0f01454884b6fecd9f00d99ba9d17956df2fd47b6f84305c77")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.22:", type=("build", "run"))
	depends_on("r-biostrings@2.44.2:", type=("build", "run"))
	depends_on("r-data-table@1.10.4.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-s4vectors@0.14.3:", type=("build", "run"))
	depends_on("r-shortread@1.34:", type=("build", "run"))
	depends_on("r-iranges@2.10.2:", type=("build", "run"))
	depends_on("r-genomicranges@1.28.4:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.12.2:", type=("build", "run"))
	depends_on("r-biocparallel@1.10.1:", type=("build", "run"))
	depends_on("r-gtable@0.2:", type=("build", "run"))
	depends_on("r-gridextra@2.2.1:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.4:", type=("build", "run"))
	depends_on("r-ggthemes@3.4:", type=("build", "run"))
	depends_on("r-waffle@0.7:", type=("build", "run"))
	depends_on("r-stringr@1.2:", type=("build", "run"))
	depends_on("r-matrixstats@0.52.2:", type=("build", "run"))
	depends_on("r-matrix@1.2.10:", type=("build", "run"))
	depends_on("r-dplyr@0.7.2:", type=("build", "run"))
	depends_on("r-rmarkdown@1.6:", type=("build", "run"))
	depends_on("r-knitr@1.16:", type=("build", "run"))
	depends_on("r-cluster@2.1.4:", type=("build", "run"))
