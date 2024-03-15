# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBsseq(RPackage):
	"""Analyze, manage and store bisulfite sequencing data.

	A collection of tools for analyzing and visualizing bisulfite sequencing
	data."""

	bioc = "bsseq"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/bsseq_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/bsseq/bsseq_1.38.0.tar.gz"]

	version("1.38.0", md5="0fee416655d94a260bf4a613b4a6321e")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-genomicranges@1.41.5:", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.19.5:", type=("build", "run"))
	depends_on("r-iranges@2.23.9:", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-data-table@1.11.8:", type=("build", "run"))
	depends_on("r-s4vectors@0.27.12:", type=("build", "run"))
	depends_on("r-r-utils@2:", type=("build", "run"))
	depends_on("r-delayedmatrixstats@1.5.2:", type=("build", "run"))
	depends_on("r-permute", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-delayedarray@0.15.16:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-hdf5array@1.19.11:", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-beachmat", type=("build", "run"))
