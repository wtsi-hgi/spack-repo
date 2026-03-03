# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumimouseidmapping(RPackage):
	"""Illumina Identifier mapping for Mouse

	This package includes mappings information between different types of Illumina IDs of Illumina Mouse chips and nuIDs. It also includes mappings of all nuIDs included in Illumina Mouse chips to RefSeq IDs with mapping qualities information.
	"""
	
	bioc = "lumiMouseIDMapping" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/lumiMouseIDMapping_1.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/lumiMouseIDMapping/lumiMouseIDMapping_1.10.0.tar.gz"]

	version("1.10.0", md5="305aba80ebf6ef4c26899302ea9e50e8")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-lumi@1.7.14:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

