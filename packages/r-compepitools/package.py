# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCompepitools(RPackage):
	"""Tools for computational epigenomics

	Tools for computational epigenomics developed for the analysis, integration and simultaneous visualization of various (epi)genomics data types across multiple genomic regions in multiple samples.
	"""
	
	bioc = "compEpiTools"

	version("1.42.0", commit="2d085fdebd4dce893c57bffc9f1a083c943b4c00")
	version("1.36.0", commit="a66a83688cb74142ae7b6ef2dac00317efa6a9e4")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-methylpipe", type=("build", "run"))
	depends_on("r-go-db", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
