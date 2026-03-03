# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTracktables(RPackage):
	"""Build IGV tracks and HTML reports

	Methods to create complex IGV genome browser sessions and dynamic IGV reports in HTML pages.
	"""
	
	bioc = "tracktables" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/tracktables_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/tracktables/tracktables_1.36.0.tar.gz"]

	version("1.36.0", md5="0726840a7d7c0252dc163cfe065cefa0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-iranges", type=("build", "run"))
	depends_on("r-genomicranges", type=("build", "run"))
	depends_on("r-xvector", type=("build", "run"))
	depends_on("r-rsamtools", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-tractor-base", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
