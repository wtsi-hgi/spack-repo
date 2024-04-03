# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGgspavis(RPackage):
	"""Visualization functions for spatially resolved transcriptomics data

	Visualization functions for spatially resolved transcriptomics datasets stored in SpatialExperiment format. Includes functions to create several types of plots for data from from spot-based (e.g. 10x Genomics Visium) and molecule-based (e.g. seqFISH) technological platforms.
	"""
	
	homepage = "https://github.com/lmweber/ggspavis"
	bioc = "ggspavis" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ggspavis_1.8.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ggspavis/ggspavis_1.8.1.tar.gz"]

	version("1.8.1", md5="8f1c36e3556ccfd88a1750a8b98e139a")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-spatialexperiment", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-ggside", type=("build", "run"))
