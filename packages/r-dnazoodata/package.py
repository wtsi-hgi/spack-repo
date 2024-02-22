# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDnazoodata(RPackage):
	"""DNA Zoo data package

	DNAZooData is a data package giving programmatic access to genome assemblies and Hi-C contact matrices uniformly processed by the [DNA Zoo Consortium](https://www.dnazoo.org/). The matrices are available in the multi-resolution `.hic` format. A URL to corrected genome assemblies in `.fastq` format is also provided to the end-user.
	"""
	
	homepage = "https://github.com/js2264/DNAZooData"
	bioc = "DNAZooData" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/DNAZooData_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/DNAZooData/DNAZooData_1.2.0.tar.gz"]

	version("1.2.0", md5="06c4b9dbbaddc3dd4dcdc51e34150aa7")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-hicexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))

	# experiment