# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrereg(RPackage):
	"""R Markdown Templates to Preregister Scientific Studies

	Provides a collection of templates to author preregistration documents for scientific studies in PDF format.
	"""
	
	homepage = "https://github.com/crsh/prereg"
	cran = "prereg" 

	version("0.6.0", md5="2ab6436c64f92282dd5bfe0910791e11")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-rmarkdown@1:", type=("build", "run"))
