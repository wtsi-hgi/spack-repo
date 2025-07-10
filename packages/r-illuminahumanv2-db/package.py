# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIlluminahumanv2Db(RPackage):
	"""Illumina HumanWG6v2 annotation data (chip illuminaHumanv2)

	Illumina HumanWG6v2 annotation data (chip illuminaHumanv2) assembled using data from public repositories
	"""
	
	bioc = "illuminaHumanv2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/illuminaHumanv2.db_1.26.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/illuminaHumanv2.db/illuminaHumanv2.db_1.26.0.tar.gz"]

	version("1.26.0", sha256="665eb75f2c3d014ead6a7765dca388becfef35cb459b94520a73d3978cc0fb8a")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.1.2:", type=("build", "run"))

