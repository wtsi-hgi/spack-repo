# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylumi(RPackage):
	"""Handle Illumina methylation data.

	This package provides classes for holding and manipulating Illumina
	methylation data. Based on eSet, it can contain MIAME information, sample
	information, feature information, and multiple matrices of data. An
	"intelligent" import function, methylumiR can read the Illumina text files
	and create a MethyLumiSet. methylumIDAT can directly read raw IDAT files
	from HumanMethylation27 and HumanMethylation450 microarrays. Normalization,
	background correction, and quality control features for GoldenGate,
	Infinium, and Infinium HD arrays are also included."""

	bioc = "methylumi"
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/methylumi_2.48.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/methylumi/methylumi_2.48.0.tar.gz"]

	version("2.48.0", md5="eb3792c8c9c2a778cf41e9bb7b95232b")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-fdb-infiniummethylation-hg19@2.2:", type=("build", "run"))
	depends_on("r-minfi", type=("build", "run"))
	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-annotate", type=("build", "run"))
	depends_on("r-genefilter", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-illuminaio", type=("build", "run"))
	depends_on("r-genomicfeatures", type=("build", "run"))
