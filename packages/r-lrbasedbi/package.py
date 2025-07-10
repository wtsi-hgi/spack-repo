# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrbasedbi(RPackage):
	"""DBI to construct LRBase-related package

	Interface to construct LRBase package (LRBase.XXX.eg.db).
	"""
	
	bioc = "LRBaseDbi" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/LRBaseDbi_2.12.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/LRBaseDbi/LRBaseDbi_2.12.1.tar.gz"]

	version("2.12.1", sha256="05cfbb83ae0cfcde057c507804fcfe809b1f3dc9669a57d6c460b2eaedc57c86")
	version("2.12.0", md5="4ed780d2b26059691bd1a1e859ca5003")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-rsqlite", type=("build", "run"))
	depends_on("r-dbi", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
