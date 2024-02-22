# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSnapcount(RPackage):
	"""R/Bioconductor Package for interfacing with Snaptron for rapid querying of expression counts

	snapcount is a client interface to the Snaptron webservices which support querying by gene name or genomic region. Results include raw expression counts derived from alignment of RNA-seq samples and/or various summarized measures of expression across one or more regions/genes per-sample (e.g. percent spliced in).
	"""
	
	homepage = "https://github.com/langmead-lab/snapcount"
	bioc = "snapcount" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/snapcount_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/snapcount/snapcount_1.14.0.tar.gz"]

	version("1.14.0", md5="8efa036bfe73acf9c31a279b3c365ae7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-assertthat", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
