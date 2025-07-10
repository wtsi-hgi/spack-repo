# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdCotton(RPackage):
	"""Platform Design Info for The Manufacturer's Name Cotton

	Platform Design Info for The Manufacturer's Name Cotton
	"""
	
	bioc = "pd.cotton" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.cotton_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.cotton/pd.cotton_3.12.0.tar.gz"]

	version("3.12.0", sha256="f4a8f5a29ec783d1ac549dbea2610f8b1ea795e1c2b3b3e09162c466379de1c0")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

