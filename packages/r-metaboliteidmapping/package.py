# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetaboliteidmapping(RPackage):
	"""Mapping of Metabolite IDs from Different Sources

	The package provides a comprehensive mapping table of nine different Metabolite ID formats and their common name. The data has been collected and merged from four publicly available source, including HMDB, Comptox Dashboard, ChEBI, and the graphite Bioconductor R package.
	"""
	
	homepage = "https://github.com/yigbt/metaboliteIDmapping"
	bioc = "metaboliteIDmapping" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/metaboliteIDmapping_1.0.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/metaboliteIDmapping/metaboliteIDmapping_1.0.0.tar.gz"]

	version("1.0.0", md5="bd78ec373ce90fac1a10d2c64c462e77")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))

