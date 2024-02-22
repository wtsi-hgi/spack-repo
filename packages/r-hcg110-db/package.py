# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHcg110Db(RPackage):
	"""Affymetrix Affymetrix HC_G110 Array annotation data (chip hcg110)

	Affymetrix Affymetrix HC_G110 Array annotation data (chip hcg110) assembled using data from public repositories
	"""
	
	bioc = "hcg110.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/hcg110.db_3.13.0.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/hcg110.db/hcg110.db_3.13.0.tar.gz"]

	version("3.13.0", md5="4c536c3539a61d7f1f67dac149f10b11")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.13:", type=("build", "run"))

	# annotation