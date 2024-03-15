# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAth1121501Db(RPackage):
	"""Affymetrix Affymetrix ATH1-121501 Array annotation data (chip ath1121501)

	Affymetrix Affymetrix ATH1-121501 Array annotation data (chip ath1121501) assembled using data from public repositories
	"""
	
	bioc = "ath1121501.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/ath1121501.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/ath1121501.db/ath1121501.db_3.13.0.tar.gz"]

	version("3.13.0", md5="c5d937ca9c6bcbb4385fb37a3b14ad15")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-at-tair-db@3.13:", type=("build", "run"))

	# annotation