# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGenvisr(RPackage):
	"""Genomic Visualizations in R

	Produce highly customizable publication quality graphics for genomic data primarily at the cohort level.
	"""
	
	bioc = "GenVisR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/GenVisR_1.34.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/GenVisR/GenVisR_1.34.0.tar.gz"]

    version("1.40.0", tag="RELEASE_3_21")
	version("1.34.0", sha256="eab26a20188f702c0ed032a20c3d2b39ddad8f10452d9336fa0020e344069b56")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-biomart@2.45.8:", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-genomicranges@1.25.4:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-gtable", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-iranges@2.7.5:", type=("build", "run"))
	depends_on("r-plyr@1.8.3:", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-viridis", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-variantannotation", type=("build", "run"))
