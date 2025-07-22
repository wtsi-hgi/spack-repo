# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnhancedvolcano(RPackage):
	"""Publication-ready volcano plots with enhanced colouring and labeling

	Volcano plots represent a useful way to visualise the results of differential expression analyses. Here, we present a highly-configurable function that produces publication-ready volcano plots. EnhancedVolcano will attempt to fit as many point labels in the plot window as possible, thus avoiding 'clogging' up the plot with labels that could not otherwise have been read. Other functionality allows the user to identify up to 4 different types of attributes in the same plot space via colour, shape, size, and shade parameter configurations.
	"""
	
	homepage = "https://github.com/kevinblighe/EnhancedVolcano"
	bioc = "EnhancedVolcano" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/EnhancedVolcano_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/EnhancedVolcano/EnhancedVolcano_1.20.0.tar.gz"]

	version("1.26.0", tag="RELEASE_3_21")
	version("1.20.0", sha256="022045337d389d76118b942efc27f078d4d7eea98175e4e300f5907a4a1afc24")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
