# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminaratv1Db(RPackage):
	"""Illumina Ratv1 annotation data (chip illuminaRatv1)

	Illumina Ratv1 annotation data (chip illuminaRatv1) assembled using data from public repositories
	"""
	
	bioc = "illuminaRatv1.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaRatv1.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaRatv1.db/illuminaRatv1.db_1.26.0.tar.gz"]

	version("1.26.0", md5="5de2324d7b96c0cdb3301ef269341aa8")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.1.2:", type=("build", "run"))

	# annotation