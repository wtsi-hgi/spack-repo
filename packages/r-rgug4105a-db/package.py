# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRgug4105aDb(RPackage):
	"""Agilent annotation data (chip rgug4105a)

	Agilent annotation data (chip rgug4105a) assembled using data from public repositories
	"""
	
	bioc = "rgug4105a.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/rgug4105a.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/rgug4105a.db/rgug4105a.db_3.2.3.tar.gz"]

	version("3.2.3", md5="3ccf354083ae36a7ae687fb8209c4e5b")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.3:", type=("build", "run"))

	# annotation