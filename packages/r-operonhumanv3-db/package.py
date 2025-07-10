# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROperonhumanv3Db(RPackage):
	"""FHCRC Nelson Lab OperonHumanV3 Annotation Data (OperonHumanV3)

	FHCRC Nelson Lab OperonHumanV3 Annotation Data (OperonHumanV3) assembled using data from public repositories
	"""
	
	bioc = "OperonHumanV3.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/OperonHumanV3.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/OperonHumanV3.db/OperonHumanV3.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="1198d0f69b2ec110582bdccccdf0a34c31f55e8f2b3d8441b962728690734f20")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

