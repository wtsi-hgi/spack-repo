# Copyright 2013-2024 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSummarizedexperiment(RPackage):
	"""SummarizedExperiment container.

	The SummarizedExperiment container contains one or more assays, each
	represented by a matrix-like object of numeric or other mode. The rows
	typically represent genomic ranges of interest and the columns represent
	samples."""

	bioc = "SummarizedExperiment"
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SummarizedExperiment_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SummarizedExperiment/SummarizedExperiment_1.32.0.tar.gz"]

	version("1.32.0", md5="cf4b430247b40acb2be8e6c9ecf3aac7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-matrixgenerics@1.1.3:", type=("build", "run"))
	depends_on("r-genomicranges@1.41.5:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-biocgenerics@0.37:", type=("build", "run"))
	depends_on("r-s4vectors@0.33.7:", type=("build", "run"))
	depends_on("r-iranges@2.23.9:", type=("build", "run"))
	depends_on("r-genomeinfodb@1.13.1:", type=("build", "run"))
	depends_on("r-s4arrays@1.1.1:", type=("build", "run"))
	depends_on("r-delayedarray@0.27.1:", type=("build", "run"))
