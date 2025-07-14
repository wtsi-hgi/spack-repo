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

	version("1.18.0", commit="bc68b97f2d458d252e600dfc41df3a946258a179")
	version("1.12.0", commit="61b5e505edb06b3f64d9340c4b78f78f4d8fbfc4")

	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))

