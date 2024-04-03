# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenxlsx2(RPackage):
	"""Read, Write and Edit 'xlsx' Files

	Simplifies the creation of 'xlsx' files by
    providing a high level interface to writing, styling and editing
    worksheets.
	"""
	
	homepage = "https://janmarvin.github.io/openxlsx2/"
	cran = "openxlsx2" 

	version("1.5", md5="84e5026b4180533f34473188bcd73f78", url="https://cran.r-project.org/src/contrib/openxlsx2_1.5.tar.gz")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-zip", type=("build", "run"))
