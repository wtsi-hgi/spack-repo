# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpectrum(RPackage):
	"""Fast Adaptive Spectral Clustering for Single and Multi-View Data

	A self-tuning spectral clustering method for single or multi-view data. 'Spectrum' uses a new type of adaptive density aware kernel that strengthens connections in the graph based on common nearest neighbours. It uses a tensor product graph data integration and diffusion procedure to integrate different data sources and reduce noise. 'Spectrum' uses either the eigengap or multimodality gap heuristics to determine the number of clusters. The method is sufficiently flexible so that a wide range of Gaussian and non-Gaussian structures can be clustered with automatic selection of K.
	"""
	
	cran = "Spectrum" 

	version("1.1", md5="b7b9dc038563aa75b4066990dbfb451c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-clusterr", type=("build", "run"))
	depends_on("r-rfast", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
