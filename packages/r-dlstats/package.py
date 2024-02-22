# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDlstats(RPackage):
	"""Download Stats of R Packages

	Monthly download stats of 'CRAN' and 'Bioconductor' packages.
	     Download stats of 'CRAN' packages is from the 'RStudio' 'CRAN mirror', see <https://cranlogs.r-pkg.org:443>.
	     'Bioconductor' package download stats is at <https://bioconductor.org/packages/stats/>.
	"""
	
	homepage = "https://github.com/GuangchuangYu/dlstats"
	cran = "dlstats" 

	version("0.1.7", md5="e300966c0b175c5ff15e6d5d7c964d1f")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
