# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethylseqdata(RPackage):
	"""Collection of Public DNA Methylation Sequencing Datasets

	Base-level (i.e. cytosine-level) counts for a collection of public bisulfite-seq datasets (e.g., WGBS and RRBS), provided as SummarizedExperiment objects with sample- and base-level metadata.
	"""
	
	bioc = "MethylSeqData" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/MethylSeqData_1.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/MethylSeqData/MethylSeqData_1.12.0.tar.gz"]

	version("1.18.0", tag="RELEASE_3_21")
	version("1.12.0", sha256="cc48d7096cf1f006aade41f8aa33d78dfaaf41df382dd152f8d61ad51428842f")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))

