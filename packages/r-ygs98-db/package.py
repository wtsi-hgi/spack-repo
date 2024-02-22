# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RYgs98Db(RPackage):
	"""Affymetrix Affymetrix YG_S98 Array annotation data (chip ygs98)

	Affymetrix Affymetrix YG_S98 Array annotation data (chip ygs98) assembled using data from public repositories
	"""
	
	bioc = "ygs98.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/ygs98.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/ygs98.db/ygs98.db_3.13.0.tar.gz"]

	version("3.13.0", md5="d21c0dc1ee0f7512ae921a501b425fd3")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-sc-sgd-db@3.13:", type=("build", "run"))

	# annotation