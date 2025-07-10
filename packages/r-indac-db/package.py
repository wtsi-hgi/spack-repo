# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIndacDb(RPackage):
	"""INDAC FlyChip_long_oligonucleotide_002 (FL002) annotation data (chip indac)

	INDAC FlyChip_long_oligonucleotide_002 (FL002) annotation data (chip indac) assembled using data from public repositories
	"""
	
	bioc = "indac.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/indac.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/indac.db/indac.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="51da35d543ade0d8568bb015ce992846a109102fcf2485104af34926a18f534a")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-dm-eg-db@3.3:", type=("build", "run"))

