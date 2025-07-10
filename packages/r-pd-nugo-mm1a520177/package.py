# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdNugoMm1a520177(RPackage):
	"""Platform Design Info for The Manufacturer's Name NuGO_Mm1a520177

	Platform Design Info for The Manufacturer's Name NuGO_Mm1a520177
	"""
	
	bioc = "pd.nugo.mm1a520177" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.nugo.mm1a520177_3.4.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.nugo.mm1a520177/pd.nugo.mm1a520177_3.4.0.tar.gz"]

	version("3.4.0", sha256="29d56120790e02a12db11bac7992bd75c970048915d6c8c5888287c0fafec814", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.nugo.mm1a520177_3.4.0.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

