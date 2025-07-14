# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRtcgatoolbox(RPackage):
	"""A new tool for exporting TCGA Firehose data

	Managing data from large scale projects such as The Cancer Genome Atlas (TCGA) for further analysis is an important and time consuming step for research projects. Several efforts, such as Firehose project, make TCGA pre-processed data publicly available via web services and data portals but it requires managing, downloading and preparing the data for following steps. We developed an open source and extensible R based data client for Firehose pre-processed data and demonstrated its use with sample case studies. Results showed that RTCGAToolbox could improve data management for researchers who are interested with TCGA data. In addition, it can be integrated with other analysis pipelines for following data analysis.
	"""
	
	homepage = "http://mksamur.github.io/RTCGAToolbox/"
	bioc = "RTCGAToolbox" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/RTCGAToolbox_2.32.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/RTCGAToolbox/RTCGAToolbox_2.32.1.tar.gz"]

    version("2.38.0", tag="RELEASE_3_21")
	version("2.32.1", sha256="98653b3fe5f863a38c5b8e2b8336f162356233518a38192db54b3c6dc15868a8")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-rvest", type=("build", "run"))
	depends_on("r-s4vectors@0.23.10:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tcgautils@1.9.4:", type=("build", "run"))
