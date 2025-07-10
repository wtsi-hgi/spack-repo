# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHuo22Db(RPackage):
	"""FHCRC Genomics Shared Resource HuO22 Annotation Data (HuO22)

	FHCRC Genomics Shared Resource HuO22 Annotation Data (HuO22) assembled using data from public repositories
	"""
	
	bioc = "HuO22.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/HuO22.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/HuO22.db/HuO22.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="4e6336774134f9e7cb5b06eff34b3396a95f19555f4078c16213e5a407a23595")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-hs-eg-db@3.3:", type=("build", "run"))

