# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdClariomSMouseHt(RPackage):
	"""Platform Design Info for Affymetrix Clariom_S_Mouse_HT

	Platform Design Info for Affymetrix Clariom_S_Mouse_HT
	"""
	
	bioc = "pd.clariom.s.mouse.ht" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.clariom.s.mouse.ht_3.14.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.clariom.s.mouse.ht/pd.clariom.s.mouse.ht_3.14.1.tar.gz"]

	version("3.14.1", md5="9cb6f77cf9666a0d54e1eacb904fd57c")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

