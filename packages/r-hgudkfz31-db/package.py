# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHgudkfz31Db(RPackage):
	"""Unknown annotation data (chip hguDKFZ31)

	Unknown annotation data (chip hguDKFZ31) assembled using data from public repositories
	"""
	
	bioc = "hguDKFZ31.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/hguDKFZ31.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/hguDKFZ31.db/hguDKFZ31.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="596d44fbd5ba386fb6a41eb5a3b3d9d87f5bc24208eec852efa4dddb64e2a0de")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

