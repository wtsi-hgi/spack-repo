# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpigenomix(RPackage):
	"""Epigenetic and gene transcription data normalization and integration with mixture models

	A package for the integrative analysis of RNA-seq or microarray based gene transcription and histone modification data obtained by ChIP-seq. The package provides methods for data preprocessing and matching as well as methods for fitting bayesian mixture models in order to detect genes with differences in both data types.
	"""
	
	bioc = "epigenomix" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/epigenomix_1.42.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/epigenomix/epigenomix_1.42.0.tar.gz"]

	version("1.48.1", tag="RELEASE_3_21")
	version("1.42.0", sha256="4b1d55e93fd0b64daa8d6dae2c1c4136c6948b4a7447dd7e4be6139e173e0523")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-mcmcpack", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-beadarray", type=("build", "run"))
