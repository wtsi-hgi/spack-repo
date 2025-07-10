# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPdHgU95c(RPackage):
	"""Platform Design Info for The Manufacturer's Name HG_U95C

	Platform Design Info for The Manufacturer's Name HG_U95C
	"""
	
	bioc = "pd.hg.u95c" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/pd.hg.u95c_3.12.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/pd.hg.u95c/pd.hg.u95c_3.12.0.tar.gz"]

	version("3.12.0", sha256="18c6667fe30adfc19513368e9fd3c6573e4540f6845ef0c76b2597c325cf3e5d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-biostrings@2.35.12:", type=("build", "run"))
	depends_on("r-rsqlite@1:", type=("build", "run"))
	depends_on("r-oligoclasses@1.29.6:", type=("build", "run"))
	depends_on("r-oligo@1.31.5:", type=("build", "run"))
	depends_on("r-dbi@0.3.1:", type=("build", "run"))
	depends_on("r-iranges@2.1.43:", type=("build", "run"))
	depends_on("r-s4vectors@0.5.22:", type=("build", "run"))

