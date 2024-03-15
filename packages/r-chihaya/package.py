# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RChihaya(RPackage):
	"""Save Delayed Operations to a HDF5 File

	Saves the delayed operations of a DelayedArray to a HDF5 file. This enables efficient recovery of the DelayedArray's contents in other languages and analysis frameworks.
	"""
	
	homepage = "https://github.com/ArtifactDB/chihaya-R"
	bioc = "chihaya" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/chihaya_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/chihaya/chihaya_1.2.0.tar.gz"]

	version("1.2.0", md5="fc8e24fa8ec373d01c938fbfe12c3b9a")

	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
