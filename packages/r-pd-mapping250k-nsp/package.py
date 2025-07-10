# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdMapping250kNsp(RPackage):
	"""Platform Design Info for Affymetrix Mapping250K_Nsp

	Platform Design Info for Affymetrix Mapping250K_Nsp
	"""
	
	bioc = "pd.mapping250k.nsp" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.mapping250k.nsp_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.mapping250k.nsp/pd.mapping250k.nsp_3.12.0.tar.gz"]

	version("3.12.0", sha256="e7374b851ab33979e902d8bacdf6c4430d6a1885047173ff016f43fa50604882")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

