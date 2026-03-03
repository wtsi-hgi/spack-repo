# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStevetemplates(RPackage):
	"""Steve's R Markdown Templates

	These are my collection of 'R Markdown' templates, mostly for compilation to PDF.
    These are useful for all things academic and professional, if you are using 'R Markdown'
    for things like your CV or your articles and manuscripts.
	"""
	
	cran = "stevetemplates" 

	version("1.0.0", md5="f88b6c80d31873b189b9fd9ec2e49aeb")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
