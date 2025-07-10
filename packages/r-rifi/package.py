# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRifi(RPackage):
	"""'rifi' analyses data from rifampicin time series created by microarray or RNAseq

	'rifi' analyses data from rifampicin time series created by microarray or RNAseq. 'rifi' is a transcriptome data analysis tool for the holistic identification of transcription and decay associated processes. The decay constants and the delay of the onset of decay is fitted for each probe/bin. Subsequently, probes/bins of equal properties are combined into segments by dynamic programming, independent of a existing genome annotation. This allows to detect transcript segments of different stability or transcriptional events within one annotated gene. In addition to the classic decay constant/half-life analysis, 'rifi' detects processing sites, transcription pausing sites, internal transcription start sites in operons, sites of partial transcription termination in operons, identifies areas of likely transcriptional interference by the collision mechanism and gives an estimate of the transcription velocity. All data are integrated to give an estimate of continous transcriptional units, i.e. operons. Comprehensive output tables and visualizations of the full genome result and the individual fits for all probes/bins are produced.
	"""
	
	bioc = "rifi" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/rifi_1.6.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/rifi/rifi_1.6.0.tar.gz"]

	version("1.6.0", sha256="82ea553367f6850b21ce41e9e1e791f269f1ed5c782a1ded795a69633ee71634")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-car", type=("build", "run"))
	depends_on("r-cowplot", type=("build", "run"))
	depends_on("r-domc", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-egg", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-nls2", type=("build", "run"))
	depends_on("r-nnet", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-tibble", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
