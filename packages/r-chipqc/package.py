# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChipqc(RPackage):
	"""Quality metrics for ChIPseq data

	Quality metrics for ChIPseq data.
	"""
	
	bioc = "ChIPQC" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/ChIPQC_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/ChIPQC/ChIPQC_1.38.0.tar.gz"]

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="123e3c006c30aa0e6327d3bfc58729c8cc3f9d7274825282011a7b28b4e89328")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-diffbind", type=("build", "run"))
	depends_on("r-genomicranges@1.17.19:", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-biocgenerics@0.11.3:", type=("build", "run"))
	depends_on("r-s4vectors@0.1:", type=("build", "run"))
	depends_on("r-iranges@1.99.17:", type=("build", "run"))
	depends_on("r-rsamtools@1.17.28:", type=("build", "run"))
	depends_on("r-genomicalignments@1.1.16:", type=("build", "run"))
	depends_on("r-chipseq@1.12:", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-nozzle-r1", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg19-knowngene", type=("build", "run"))
	depends_on("r-txdb-hsapiens-ucsc-hg18-knowngene", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm10-knowngene", type=("build", "run"))
	depends_on("r-txdb-mmusculus-ucsc-mm9-knowngene", type=("build", "run"))
	depends_on("r-txdb-rnorvegicus-ucsc-rn4-ensgene", type=("build", "run"))
	depends_on("r-txdb-celegans-ucsc-ce6-ensgene", type=("build", "run"))
	depends_on("r-txdb-dmelanogaster-ucsc-dm3-ensgene", type=("build", "run"))
