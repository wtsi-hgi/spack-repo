# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanv1Db(RPackage):
	"""Illumina HumanWG6v1 annotation data (chip illuminaHumanv1)

	Illumina HumanWG6v1 annotation data (chip illuminaHumanv1) assembled using data from public repositories
	"""
	
	bioc = "illuminaHumanv1.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaHumanv1.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaHumanv1.db/illuminaHumanv1.db_1.26.0.tar.gz"]

	version("1.26.0", md5="2c362256b7be2861b8bf6e0d1fe46786")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.1.2:", type=("build", "run"))

	# annotation