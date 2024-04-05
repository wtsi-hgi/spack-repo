# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdRta10(RPackage):
	"""Platform Design Info for Affymetrix RTA-1_0

	Platform Design Info for Affymetrix RTA-1_0
	"""
	
	bioc = "pd.rta.1.0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.rta.1.0_3.12.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.rta.1.0/pd.rta.1.0_3.12.2.tar.gz"]

	version("3.12.2", md5="90752a892a103c7fe4cd6c86e61a61db", url="https://www.bioconductor.org/packages/release/data/annotation/src/contrib/pd.rta.1.0_3.12.2.tar.gz")
	version("3.12.2", md5="90752a892a103c7fe4cd6c86e61a61db", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.rta.1.0_3.12.2.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

