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

	version("1.26.0", commit="e2756f5de3a4af4b5cbee11912879fd94795b3ca")
	version("1.20.0", commit="f0abfa52c086dc1804b4c720ef5af6dd674532ba")

	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggrepel", type=("build", "run"))
