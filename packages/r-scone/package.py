# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScone(RPackage):
	"""Single Cell Overview of Normalized Expression data

	SCONE is an R package for comparing and ranking the performance of different normalization schemes for single-cell RNA-seq and other high-throughput analyses.
	"""
	
	bioc = "scone" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/scone_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/scone/scone_1.26.0.tar.gz"]

	version("1.26.0", md5="0e7dd77999fc8cbf842fee6452c82a1b")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-aroma-light", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-cluster", type=("build", "run"))
	depends_on("r-compositions", type=("build", "run"))
	depends_on("r-diptest", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-fpc", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-mixtools", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-boot", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-ruvseq", type=("build", "run"))
	depends_on("r-rarpack", type=("build", "run"))
	depends_on("r-matrixgenerics", type=("build", "run"))
	depends_on("r-singlecellexperiment", type=("build", "run"))
