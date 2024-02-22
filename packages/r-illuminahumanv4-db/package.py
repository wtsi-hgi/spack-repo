# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanv4Db(RPackage):
	"""Illumina HumanHT12v4 annotation data (chip illuminaHumanv4)

	Illumina HumanHT12v4 annotation data (chip illuminaHumanv4) assembled using data from public repositories
	"""
	
	bioc = "illuminaHumanv4.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/illuminaHumanv4.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/illuminaHumanv4.db/illuminaHumanv4.db_1.26.0.tar.gz"]

	version("1.26.0", md5="42d554559ac0106dc71317ffaf466421")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.1.2:", type=("build", "run"))

	# annotation