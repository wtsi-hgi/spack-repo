# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPulsetd(RPackage):
	"""Identification of Transcriptional Dynamics using Pulse Models
via 4su-Seq Data and RNA-Seq Data

	A tool for analyzing the transcription, processing and degradation rates of genes by 4sU-seq (the Metabolic Label 4-thiouridine) data and RNA-seq (RNA sequencing) data. It can not only recognize the transcriptional dynamic rates at the measurement time points, but also obtain continuous changes in transcriptional dynamics. More importantly, it is able to predict the trend of mRNA (Mature RNA) transcription and expression changes in the future.
	"""
	
	homepage = "https://github.com/bioWzz/pulseTD_0.1.0"
	cran = "pulseTD" 

	version("0.1.0", md5="a8cf1c7ec53b4a183c274af5da15d3e1")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
