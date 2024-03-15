# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBiovizbase(RPackage):
	"""Basic graphic utilities for visualization of genomic data.

	The biovizBase package is designed to provide a set of utilities, color
	schemes and conventions for genomic data. It serves as the base for
	various high-level packages for biological data visualization. This
	saves development effort and encourages consistency."""

	bioc = "biovizBase"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/biovizBase_1.50.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/biovizBase/biovizBase_1.50.0.tar.gz"]

	version("1.50.0", md5="8430b2a7913fdcfe27b9bf52ba9aff7e")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-dichromat", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors@0.23.19:", type=("build", "run"))
	depends_on("r-iranges@1.99.28:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.5.14:", type=("build", "run"))
	depends_on("r-genomicranges@1.23.21:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-biostrings@2.33.11:", type=("build", "run"))
	depends_on("r-rsamtools@1.17.28:", type=("build", "run"))
	depends_on("r-genomicalignments@1.1.16:", type=("build", "run"))
	depends_on("r-genomicfeatures@1.21.19:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-variantannotation@1.11.4:", type=("build", "run"))
	depends_on("r-ensembldb@1.99.13:", type=("build", "run"))
	depends_on("r-annotationfilter@0.99.8:", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
