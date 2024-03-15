# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdHta20(RPackage):
	"""Platform Design Info for Affymetrix HTA-2_0

	Platform Design Info for Affymetrix HTA-2_0
	"""
	
	bioc = "pd.hta.2.0" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.hta.2.0_3.12.2.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.hta.2.0/pd.hta.2.0_3.12.2.tar.gz"]

	version("3.12.2", md5="8e13f85ece49c38da73eaf7b2247f5f0", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.hta.2.0_3.12.2.tar.gz")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

	# annotation