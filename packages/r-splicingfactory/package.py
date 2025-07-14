# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSplicingfactory(RPackage):
	"""Splicing Diversity Analysis for Transcriptome Data

	The SplicingFactory R package uses transcript-level expression values to analyze splicing diversity based on various statistical measures, like Shannon entropy or the Gini index. These measures can quantify transcript isoform diversity within samples or between conditions. Additionally, the package analyzes the isoform diversity data, looking for significant changes between conditions.
	"""
	
	homepage = "https://github.com/esebesty/SplicingFactory"
	bioc = "SplicingFactory"

	version("1.16.0", commit="e61e5e72a5959b66109fa637341ae11b4efbb9f7")
	version("1.10.0", commit="83e7e19bf422add246869ce781af5115d5bd2acc")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
