# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanwgdaslv4Db(RPackage):
	"""Illumina HumanWGDASLv4 annotation data (chip illuminaHumanWGDASLv4)

	Illumina HumanWGDASLv4 annotation data (chip illuminaHumanWGDASLv4) assembled using data from public repositories
	"""
	
	bioc = "illuminaHumanWGDASLv4.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaHumanWGDASLv4.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaHumanWGDASLv4.db/illuminaHumanWGDASLv4.db_1.26.0.tar.gz"]

	version("1.26.0", md5="4cc1f192de838f2b6c1b148706d354ca")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.1.2:", type=("build", "run"))

