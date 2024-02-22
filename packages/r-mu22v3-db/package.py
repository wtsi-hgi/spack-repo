# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMu22v3Db(RPackage):
	"""FHCRC Genomics Shared Resource Mu22v3 Annotation Data (Mu22v3)

	FHCRC Genomics Shared Resource Mu22v3 Annotation Data (Mu22v3) assembled using data from public repositories
	"""
	
	bioc = "Mu22v3.db" 
	urls = ["https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Mu22v3.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/release/data/annotation/src/contrib/Archive/Mu22v3.db/Mu22v3.db_3.2.3.tar.gz"]

	version("3.2.3", md5="44aaebe909be9b0108256194c55cf6fb")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))

	# annotation