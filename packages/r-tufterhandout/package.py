# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTufterhandout(RPackage):
	"""Tufte-style html document format for rmarkdown

	Custom template and output formats for use with rmarkdown. Produce
    Edward Tufte-style handouts in html formats with full support for rmarkdown
    features
	"""
	
	homepage = "http://sachsmc.github.io/tufterhandout"
	cran = "tufterhandout" 

	version("1.2.1", md5="133fc220d1eb25b4cc44d929c9bb360a")

	depends_on("r-rmarkdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
