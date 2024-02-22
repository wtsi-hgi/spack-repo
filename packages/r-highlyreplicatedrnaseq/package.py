# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHighlyreplicatedrnaseq(RPackage):
	"""Collection of Bulk RNA-Seq Experiments With Many Replicates

	Gene-level count matrix data for bulk RNA-seq dataset with many replicates. The data are provided as easy to use SummarizedExperiment objects. The source data that is made accessible through this package comes from https://github.com/bartongroup/profDGE48.
	"""
	
	homepage = "https://github.com/const-ae/HighlyReplicatedRNASeq"
	bioc = "HighlyReplicatedRNASeq" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/HighlyReplicatedRNASeq_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/HighlyReplicatedRNASeq/HighlyReplicatedRNASeq_1.14.0.tar.gz"]

	version("1.14.0", md5="a397cddffb2dfea70943930b992ea7c0")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))

	# experiment