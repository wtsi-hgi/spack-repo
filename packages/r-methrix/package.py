# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMethrix(RPackage):
	"""Fast and efficient summarization of generic bedGraph files from Bisufite sequencing

	Bedgraph files generated by Bisulfite pipelines often come in various flavors. Critical downstream step requires summarization of these files into methylation/coverage matrices. This step of data aggregation is done by Methrix, including many other useful downstream functions.
	"""
	
	homepage = "https://github.com/CompEpigen/methrix"
	bioc = "methrix" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/methrix_1.16.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/methrix/methrix_1.16.0.tar.gz"]

	version("1.16.0", md5="7bdda59fc802fc09d10ca9a4916cfe94")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-rtracklayer", type=("build", "run"))
	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-bsgenome", type=("build", "run"))
	depends_on("r-delayedmatrixstats", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-matrixstats", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
