# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHi16codDb(RPackage):
	"""Codelink Human Inflammation 16 Bioarray annotation data (chip hi16cod)

	Codelink Human Inflammation 16 Bioarray annotation data (chip hi16cod) assembled using data from public repositories
	"""
	
	bioc = "hi16cod.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hi16cod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hi16cod.db/hi16cod.db_3.4.0.tar.gz"]

	version("3.4.0", md5="abdc77937e8d37fa5468691376ceb6a5")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.2.1:", type=("build", "run"))

