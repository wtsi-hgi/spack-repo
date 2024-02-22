# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterMatrix(RPackage):
	"""Load and Save Artifacts from File

	Save matrices, arrays and similar objects into file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.matrix" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/alabaster.matrix_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/alabaster.matrix/alabaster.matrix_1.2.0.tar.gz"]

	version("1.2.0", md5="099a01bbb4a95bdaf0f91ffd2b89653d")

	depends_on("r-biocgenerics", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-delayedarray@0.27.2:", type=("build", "run"))
	depends_on("r-sparsearray", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-hdf5array", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
