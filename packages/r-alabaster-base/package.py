# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterBase(RPackage):
	"""Save Bioconductor Objects To File

	Save Bioconductor data structures into file artifacts, and load them back into memory. This is a more robust and portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.base" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/alabaster.base_1.2.1.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/alabaster.base/alabaster.base_1.2.1.tar.gz"]

	version("1.2.1", md5="2d6215dfe9b8412438f9b05b54be2331")

	depends_on("r-alabaster-schemas", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-rhdf5", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-jsonvalidate", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rhdf5lib", type=("build", "run"))
	depends_on("zlib", type=("build", "link", "run"))
	depends_on("gzip", type=("build", "link", "run"))
