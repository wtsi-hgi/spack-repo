# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterString(RPackage):
	"""Save and Load Biostrings to/from File

	Save Biostrings objects to file artifacts, and load them back into memory. This is a more portable alternative to serialization of such objects into RDS files. Each artifact is associated with metadata for further interpretation; downstream applications can enrich this metadata with context-specific properties.
	"""
	
	bioc = "alabaster.string" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/alabaster.string_1.2.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/alabaster.string/alabaster.string_1.2.0.tar.gz"]

	version("1.2.0", md5="b7add7aa52b8835471b04038842da095")

	depends_on("r-biostrings", type=("build", "run"))
	depends_on("r-alabaster-base", type=("build", "run"))
