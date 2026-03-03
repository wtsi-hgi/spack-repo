# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RH5vc(RPackage):
	"""Managing alignment tallies using a hdf5 backend

	This package contains functions to interact with tally data from NGS experiments that is stored in HDF5 files.
	"""
	
	bioc = "h5vc" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/h5vc_2.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/h5vc/h5vc_2.36.0.tar.gz"]

	version("2.36.0", md5="2d827ac4606ef723005e479de8540b7a")

	depends_on("r-gridextra", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-reshape", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-rsamtools@2.13.1:", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-batchjobs", type=("build", "run"))
	depends_on("r-h5vcdata", type=("build", "run"))
	depends_on("r-genomeinfodb", type=("build", "run"))
	depends_on("r-rhtslib@1.99.1:", type=("build", "run"))
	depends_on("bzip2", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("xz", type=("build", "link", "run"))
	depends_on("zlib", type=("build", "link", "run"))
