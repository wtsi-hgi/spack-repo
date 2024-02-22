# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAmerifluxr(RPackage):
	"""Interface to 'AmeriFlux' Data Services

	Programmatic interface to the 'AmeriFlux' database
    (<https://ameriflux.lbl.gov/>). Provide query, download,
    and data summary tools.
	"""
	
	homepage = "https://github.com/chuhousen/amerifluxr"
	cran = "amerifluxr" 

	version("1.0.0", md5="104b7337c1657e30c8f5e279da85f038")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-heatmaply", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-memoise", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
