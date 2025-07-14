# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMicrostasis(RPackage):
	"""Microbiota STability ASsessment via Iterative cluStering

	The toolkit 'µSTASIS', or microSTASIS, has been developed for the stability analysis of microbiota in a temporal framework by leveraging on iterative clustering. Concretely, the core function uses Hartigan-Wong k-means algorithm as many times as possible for stressing out paired samples from the same individuals to test if they remain together for multiple numbers of clusters over a whole data set of individuals. Moreover, the package includes multiple functions to subset samples from paired times, validate the results or visualize the output.
	"""
	
	homepage = "https://doi.org/10.1093/bib/bbac055"
	bioc = "microSTASIS"

	version("1.8.0", commit="9539f1cc829644285a0c265558bc247aadcc2330")
	version("1.2.0", commit="a3057b219688442e8b61bbfd6db50ffda9831aeb")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-ggside", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-treesummarizedexperiment", type=("build", "run"))
