# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNugohs1a520180Db(RPackage):
	"""Affymetrix nugohs1a520180 annotation data (chip nugohs1a520180)

	Affymetrix nugohs1a520180 annotation data (chip nugohs1a520180) assembled using data from public repositories
	"""
	
	bioc = "nugohs1a520180.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/nugohs1a520180.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/nugohs1a520180.db/nugohs1a520180.db_3.4.0.tar.gz"]

	version("3.4.0", md5="f83701b35b07e69e1ad503b546bb5eaf")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.2.1:", type=("build", "run"))

