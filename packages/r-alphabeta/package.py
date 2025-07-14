# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlphabeta(RPackage):
	"""Computational inference of epimutation rates and spectra from high-throughput DNA methylation data in plants

	AlphaBeta is a computational method for estimating epimutation rates and spectra from high-throughput DNA methylation data in plants. The method has been specifically designed to: 1. analyze 'germline' epimutations in the context of multi-generational mutation accumulation lines (MA-lines). 2. analyze 'somatic' epimutations in the context of plant development and aging.
	"""
	
	bioc = "AlphaBeta"

	version("1.22.0", commit="af38811b93b19d0956ec40adc7ca544f61cd3e12")
	version("1.16.0", commit="f045eef05b59e50e3b12df2501510285ee3c2806")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-dplyr@0.7:", type=("build", "run"))
	depends_on("r-data-table@1.10:", type=("build", "run"))
	depends_on("r-stringr@1.3:", type=("build", "run"))
	depends_on("r-gtools@3.8:", type=("build", "run"))
	depends_on("r-optimx@2018.7.10:", type=("build", "run"))
	depends_on("r-expm@0.999.4:", type=("build", "run"))
	depends_on("r-biocparallel@1.18:", type=("build", "run"))
	depends_on("r-igraph@1.2.4:", type=("build", "run"))
	depends_on("r-ggplot2@3.2:", type=("build", "run"))
	depends_on("r-plotly@4.9:", type=("build", "run"))
