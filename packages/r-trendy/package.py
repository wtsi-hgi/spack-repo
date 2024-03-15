# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrendy(RPackage):
	"""Breakpoint analysis of time-course expression data

	Trendy implements segmented (or breakpoint) regression models to estimate breakpoints which represent changes in expression for each feature/gene in high throughput data with ordered conditions.
	"""
	
	homepage = "https://github.com/rhondabacher/Trendy"
	bioc = "Trendy" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Trendy_1.24.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/Trendy/Trendy_1.24.1.tar.gz"]

	version("1.24.1", md5="00e5de9c46c116f4adc3caf3708608df")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-segmented", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyfiles", type=("build", "run"))
