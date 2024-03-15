# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanv3Db(RPackage):
	"""Illumina HumanHT12v3 annotation data (chip illuminaHumanv3)

	Illumina HumanHT12v3 annotation data (chip illuminaHumanv3) assembled using data from public repositories
	"""
	
	bioc = "illuminaHumanv3.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaHumanv3.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaHumanv3.db/illuminaHumanv3.db_1.26.0.tar.gz"]

	version("1.26.0", md5="7d9e7534f0b60f0e3e7473e545ef373d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.1.2:", type=("build", "run"))

	# annotation