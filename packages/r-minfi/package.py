# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMinfi(RPackage):
	"""Analyze Illumina Infinium DNA methylation arrays.

	Tools to analyze & visualize Illumina Infinium methylation arrays."""

	bioc = "minfi"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/minfi_1.48.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/minfi/minfi_1.48.0.tar.gz"]

	version("1.48.0", md5="3c1998eee0aabbfab3c3796c82339a18")

	depends_on("r-biocgenerics@0.15.3:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment@1.1.6:", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-bumphunter@1.1.9:", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-biobase@2.33.2:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-beanplot", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-nor1mix", type=("build", "run"))
	depends_on("r-siggenes", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-preprocesscore", type=("build", "run"))
	depends_on("r-illuminaio@0.23.2:", type=("build", "run"))
	depends_on("r-delayedmatrixstats@1.3.4:", type=("build", "run"))
	depends_on("r-mclust", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-nlme", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-quadprog", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-geoquery", type=("build", "run"))
	depends_on("r-delayedarray@0.15.16:", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
