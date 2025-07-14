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

	version("1.8.0", commit="8cb7246984b9c3a63dd90e092e19837664b6e4af")
	version("1.2.0", commit="226f0349b7d16d189bdb6e180bbd7b3b14d05fae")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-hicexperiment", type=("build", "run"))
	depends_on("r-biocfilecache", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rjson", type=("build", "run"))

