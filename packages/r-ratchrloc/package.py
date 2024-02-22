# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRatchrloc(RPackage):
	"""A data package containing annotation data for ratCHRLOC

	Annotation data file for ratCHRLOC assembled using data from public data repositories
	"""
	
	bioc = "ratCHRLOC" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ratCHRLOC_2.1.6.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ratCHRLOC/ratCHRLOC_2.1.6.tar.gz"]

	version("2.1.6", md5="6fecff4821a5a47e3bd38a2ff78173d5")

	depends_on("r@2.7:", type=("build", "run"))

	# annotation