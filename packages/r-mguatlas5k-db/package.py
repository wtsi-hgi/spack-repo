# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMguatlas5kDb(RPackage):
	"""Clontech BD Atlas Long Oligos Mouse 5K annotation data (chip mguatlas5k)

	Clontech BD Atlas Long Oligos Mouse 5K annotation data (chip mguatlas5k) assembled using data from public repositories
	"""
	
	bioc = "mguatlas5k.db" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/mguatlas5k.db_3.2.3.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/mguatlas5k.db/mguatlas5k.db_3.2.3.tar.gz"]

	version("3.2.3", sha256="39b9c102c6d1cc771183cfeb0c19565acaac1d6d642481f035805d9eb2009c22")

	depends_on("r@2.7:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-org-mm-eg-db@3.3:", type=("build", "run"))

