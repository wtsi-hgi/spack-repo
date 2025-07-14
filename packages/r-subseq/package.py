# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSubseq(RPackage):
	"""Subsampling of high-throughput sequencing count data

	Subsampling of high throughput sequencing count data for use in experiment design and analysis.
	"""
	
	homepage = "http://github.com/StoreyLab/subSeq"
	bioc = "subSeq" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/subSeq_1.32.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/subSeq/subSeq_1.32.0.tar.gz"]

    version("1.38.0", tag="RELEASE_3_21")
	version("1.32.0", sha256="02c0f0531375c2dadf3b1c86859886eb469bb7595f7e8deb5e5ea5c355cf0878")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-tidyr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-qvalue@1.99:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
