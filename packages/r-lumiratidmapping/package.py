# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLumiratidmapping(RPackage):
	"""Illumina Identifier mapping for Rat

	This package includes mappings information between different types of Illumina IDs of Illumina Rat chips and nuIDs. It also includes mappings of all nuIDs included in Illumina Rat chips to RefSeq IDs with mapping qualities information.
	"""
	
	bioc = "lumiRatIDMapping" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/lumiRatIDMapping_1.10.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/lumiRatIDMapping/lumiRatIDMapping_1.10.0.tar.gz"]

	version("1.10.0", md5="1122fc25e3fff62678bed36f9d7b5709")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-lumi@1.7.14:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))

	# annotation