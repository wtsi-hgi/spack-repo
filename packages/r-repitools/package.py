# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepitools(RPackage):
	"""Epigenomic tools

	Tools for the analysis of enrichment-based epigenomic data.  Features include summarization and visualization of epigenomic data across promoters according to gene expression context, finding regions of differential methylation/binding, BayMeth for quantifying methylation etc.
	"""
	
	bioc = "Repitools"

	version("1.54.0", commit="5f0efc78e7686651a675edb50af94cba59017010")
	version("1.48.0", commit="2513661d6304ae55f7cac6e8ed2352d9d37effbc")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-biocgenerics@0.8:", type=("build", "run"))
	depends_on("r-s4vectors@0.17.25:", type=("build", "run"))
	depends_on("r-iranges@2.13.12:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-bsgenome@1.47.3:", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-gsmoothr", type=("build", "run"))
	depends_on("r-edger@3.4:", type=("build", "run"))
	depends_on("r-dnacopy", type=("build", "run"))
	depends_on("r-ringo", type=("build", "run"))
	depends_on("r-rsolnp", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
