# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRae230bDb(RPackage):
	"""Affymetrix Affymetrix RAE230B Array annotation data (chip rae230b)

	Affymetrix Affymetrix RAE230B Array annotation data (chip rae230b) assembled using data from public repositories
	"""
	
	bioc = "rae230b.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/rae230b.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/rae230b.db/rae230b.db_3.13.0.tar.gz"]

	version("3.13.0", md5="4f0474ed22bf5ebd932dd6a4d9573551")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-rn-eg-db@3.13:", type=("build", "run"))

	# annotation