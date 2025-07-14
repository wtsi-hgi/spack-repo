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

	version("1.8.0", tag="RELEASE_3_21")
	version("1.2.0", sha256="f193f2c53109a931b6a44f8931e6ba6dc463ae180c452d1b6d137d32e13de255")

	depends_on("r-delayedarray", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
