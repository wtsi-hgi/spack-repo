# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumihumanidmapping(RPackage):
	"""Illumina Identifier mapping for Human

	This package includes mappings information between different types of Illumina IDs of Illumina Human chips and nuIDs. It also includes mappings of all nuIDs included in Illumina Human chips to RefSeq IDs with mapping qualities information.
	"""
	
	bioc = "lumiHumanIDMapping" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/lumiHumanIDMapping_1.10.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/lumiHumanIDMapping/lumiHumanIDMapping_1.10.1.tar.gz"]

	version("1.10.1", sha256="6414e94a243eea6a126e582a68fadd41798bb5fccc03fcc99380a01f40634948")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-lumi@1.7.14:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))

