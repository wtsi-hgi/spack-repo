# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagene(RPackage):
	"""A package to produce metagene plots

	This package produces metagene plots to compare the behavior of DNA-interacting proteins at selected groups of genes/features. Bam files are used to increase the resolution. Multiple combination of group of bam files and/or group of genomic regions can be compared in a single analysis. Bootstraping analysis is used to compare the groups and locate regions with statistically different enrichment profiles.
	"""
	
	bioc = "metagene" 

	version("2.34.0", commit="088f7efc9a9e78dcd607f0c9c62a6a4bce34c6fe")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6@2:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-ensdb-hsapiens-v86", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
