# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMwgcodDb(RPackage):
	"""Codelink Mouse Whole Genome Bioarray (~36 000 mouse gene targets) annotation data (chip mwgcod)

	Codelink Mouse Whole Genome Bioarray (~36 000 mouse gene targets) annotation data (chip mwgcod) assembled using data from public repositories
	"""
	
	bioc = "mwgcod.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mwgcod.db_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mwgcod.db/mwgcod.db_3.4.0.tar.gz"]

	version("3.4.0", md5="3d6e2af6b05d6e07a212c043dc9d37c4")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.2.1:", type=("build", "run"))

