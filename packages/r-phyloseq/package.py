# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPhyloseq(RPackage):
	"""Handling and analysis of high-throughput microbiome census data.

	phyloseq provides a set of classes and tools to facilitate the import,
	storage, analysis, and graphical display of microbiome census data."""

	bioc = "phyloseq"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/phyloseq_1.46.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/phyloseq/phyloseq_1.46.0.tar.gz"]

	version("1.46.0", md5="335dc9dedba529ce34669dd881127e7c")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ade4@1.7.4:", type=("build", "run"))
	depends_on("r-ape@5:", type=("build", "run"))
	depends_on("r-biobase@2.36.2:", type=("build", "run"))
	depends_on("r-biocgenerics@0.22:", type=("build", "run"))
	depends_on("r-biomformat@1:", type=("build", "run"))
	depends_on("r-biostrings@2.40:", type=("build", "run"))
	depends_on("r-cluster@2.0.4:", type=("build", "run"))
	depends_on("r-data-table@1.10.4:", type=("build", "run"))
	depends_on("r-foreach@1.4.3:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-igraph@1.0.1:", type=("build", "run"))
	depends_on("r-multtest@2.28:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-reshape2@1.4.1:", type=("build", "run"))
	depends_on("r-scales@0.4:", type=("build", "run"))
	depends_on("r-vegan@2.5:", type=("build", "run"))
