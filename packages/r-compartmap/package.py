# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompartmap(RPackage):
	"""Higher-order chromatin domain inference in single cells from scRNA-seq and scATAC-seq

	Compartmap performs direct inference of higher-order chromatin from scRNA-seq and scATAC-seq. This package implements a James-Stein estimator for computing single-cell level higher-order chromatin domains. Further, we utilize random matrix theory as a method to de-noise correlation matrices to achieve a similar "plaid-like" patterning as observed in Hi-C and scHi-C data.
	"""
	
	homepage = "https://github.com/biobenkj/compartmap"
	bioc = "compartmap" 

	version("1.20.0", commit="4538ef12f5cc16a138979075b9322b2b2d5d1ee1")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-raggedexperiment", type=("build", "run"))
	depends_on("r-biocsingular", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rmtstat", type=("build", "run"))
