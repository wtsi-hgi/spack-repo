# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAgDb(RPackage):
	"""Affymetrix Affymetrix AG Array annotation data (chip ag)

	Affymetrix Affymetrix AG Array annotation data (chip ag) assembled using data from public repositories
	"""
	
	bioc = "ag.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ag.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ag.db/ag.db_3.13.0.tar.gz"]

	version("3.13.0", sha256="f0bf2ba9f4d34c581dbee85302dac01b9a14d2677f46e9436e1631892127be00")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-at-tair-db@3.13:", type=("build", "run"))

