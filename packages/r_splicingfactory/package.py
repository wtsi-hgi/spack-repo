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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SplicingFactory_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SplicingFactory/SplicingFactory_1.10.0.tar.gz"]

	version("1.10.0", md5="354167193190b04ec94fac9c097b4503")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
