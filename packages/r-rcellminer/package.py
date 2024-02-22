# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcellminer(RPackage):
	"""rcellminer: Molecular Profiles, Drug Response, and Chemical Structures for the NCI-60 Cell Lines

	The NCI-60 cancer cell line panel has been used over the course of several decades as an anti-cancer drug screen. This panel was developed as part of the Developmental Therapeutics Program (DTP, http://dtp.nci.nih.gov/) of the U.S. National Cancer Institute (NCI). Thousands of compounds have been tested on the NCI-60, which have been extensively characterized by many platforms for gene and protein expression, copy number, mutation, and others (Reinhold, et al., 2012). The purpose of the CellMiner project (http://discover.nci.nih.gov/ cellminer) has been to integrate data from multiple platforms used to analyze the NCI-60 and to provide a powerful suite of tools for exploration of NCI-60 data.
	"""
	
	homepage = "http://discover.nci.nih.gov/cellminer/"
	bioc = "rcellminer" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/rcellminer_2.24.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/rcellminer/rcellminer_2.24.0.tar.gz"]

	version("2.24.0", md5="e74fd74daff68802d805b6bc0336499d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-rcellminerdata@2:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
