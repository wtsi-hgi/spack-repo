# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsstatstmt(RPackage):
	"""Protein Significance Analysis in shotgun mass spectrometry-based proteomic experiments with tandem mass tag (TMT) labeling

	The package provides statistical tools for detecting differentially abundant proteins in shotgun mass spectrometry-based proteomic experiments with tandem mass tag (TMT) labeling. It provides multiple functionalities, including aata visualization, protein quantification and normalization, and statistical modeling and inference. Furthermore, it is inter-operable with other data processing tools, such as Proteome Discoverer, MaxQuant, OpenMS and SpectroMine.
	"""
	
	homepage = "http://msstats.org/msstatstmt/"
	bioc = "MSstatsTMT" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/MSstatsTMT_2.10.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/MSstatsTMT/MSstatsTMT_2.10.0.tar.gz"]

	version("2.10.0", md5="73166086fd3882b4771350fde01f37fb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-lmertest", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-msstats", type=("build", "run"))
	depends_on("r-msstatsconvert", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
