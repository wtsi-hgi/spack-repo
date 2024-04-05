# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdDrosophila2(RPackage):
	"""Platform Design Info for The Manufacturer's Name Drosophila_2

	Platform Design Info for The Manufacturer's Name Drosophila_2
	"""
	
	bioc = "pd.drosophila.2" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.drosophila.2_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.drosophila.2/pd.drosophila.2_3.12.0.tar.gz"]

	version("3.12.0", md5="ddb821e35e722af8dcf0807c6da4fac1", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.drosophila.2_3.12.0.tar.gz")
	version("3.12.0", md5="ddb821e35e722af8dcf0807c6da4fac1", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.drosophila.2_3.12.0.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

