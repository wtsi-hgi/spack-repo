# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChimeraviz(RPackage):
	"""Visualization tools for gene fusions

	chimeraviz manages data from fusion gene finders and provides useful visualization tools.
	"""
	
	homepage = "https://github.com/stianlagstad/chimeraviz"
	bioc = "chimeraviz"

	version("1.34.0", commit="ab42b3e90ff8817b2646a34502a946c3333c63fe")
	version("1.28.0", commit="2a2ebf38cb430ff624cda5465b77985339ca1f07")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-gviz", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-ensembldb", type=("build", "run"))
	depends_on("r-annotationfilter", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicalignments", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rcircos", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-graph", type=("build", "run"))
	depends_on("r-rgraphviz", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-biocstyle", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-magick", type=("build", "run"))
	depends_on("bowtie", type=("build", "link", "run"))
	depends_on("samtools", type=("build", "link", "run"))
