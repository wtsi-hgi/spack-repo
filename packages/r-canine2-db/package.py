# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCanine2Db(RPackage):
	"""Affymetrix Affymetrix Canine_2 Array annotation data (chip canine2)

	Affymetrix Affymetrix Canine_2 Array annotation data (chip canine2) assembled using data from public repositories
	"""
	
	bioc = "canine2.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/canine2.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/canine2.db/canine2.db_3.13.0.tar.gz"]

	version("3.13.0", md5="24727f27cdf1e324f097a76db81dfc1d")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-cf-eg-db@3.13:", type=("build", "run"))

