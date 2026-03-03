# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSetools(RPackage):
	"""SEtools: tools for working with SummarizedExperiment

	This includes a set of convenience functions for working with the SummarizedExperiment class. Note that plotting functions historically in this package have been moved to the sechm package (see vignette for details).
	"""
	
	bioc = "SEtools" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SEtools_1.16.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SEtools/SEtools_1.16.0.tar.gz"]

	version("1.16.0", md5="4b6f28a6fdf032d51f29793f25729114")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-sechm", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-deseq2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-openxlsx", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-circlize", type=("build", "run"))
	depends_on("r-sva", type=("build", "run"))
