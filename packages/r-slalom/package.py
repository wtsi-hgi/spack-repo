# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlalom(RPackage):
	"""Factorial Latent Variable Modeling of Single-Cell RNA-Seq Data

	slalom is a scalable modelling framework for single-cell RNA-seq data that uses gene set annotations to dissect single-cell transcriptome heterogeneity, thereby allowing to identify biological drivers of cell-to-cell variability and model confounding factors. The method uses Bayesian factor analysis with a latent variable model to identify active pathways (selected by the user, e.g. KEGG pathways) that explain variation in a single-cell RNA-seq dataset. This an R/C++ implementation of the f-scLVM Python package. See the publication describing the method at https://doi.org/10.1186/s13059-017-1334-8.
	"""
	
	bioc = "slalom"

	version("1.30.0", commit="3b224d47bd4391b2139321b714490c00e05830d2")
	version("1.24.0", commit="6ff8b4c2ebd71818dda9830421ac81c9938f863e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gseabase", type=("build", "run"))
	depends_on("r-rsvd", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
