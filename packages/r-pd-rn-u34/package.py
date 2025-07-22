# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdRnU34(RPackage):
	"""Platform Design Info for The Manufacturer's Name RN_U34

	Platform Design Info for The Manufacturer's Name RN_U34
	"""
	
	bioc = "pd.rn.u34" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.rn.u34_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.rn.u34/pd.rn.u34_3.12.0.tar.gz"]

	version("3.12.0", sha256="8e03ed9863d0d11df5b62cbf689e7c57117d23c1b325ec6858c1dcf34f36d72b", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.rn.u34_3.12.0.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

