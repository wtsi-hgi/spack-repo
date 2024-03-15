# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanwgdaslv3Db(RPackage):
	"""Illumina HumanHT12WGDASLv3 annotation data (chip illuminaHumanWGDASLv3)

	Illumina HumanHT12WGDASLv3 annotation data (chip illuminaHumanWGDASLv3) assembled using data from public repositories
	"""
	
	bioc = "illuminaHumanWGDASLv3.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaHumanWGDASLv3.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaHumanWGDASLv3.db/illuminaHumanWGDASLv3.db_1.26.0.tar.gz"]

	version("1.26.0", md5="32e8e24555c16f6d0148438d4a841ab8")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.1.2:", type=("build", "run"))

	# annotation