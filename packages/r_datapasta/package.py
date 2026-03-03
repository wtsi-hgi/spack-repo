# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatapasta(RPackage):
	"""R Tools for Data Copy-Pasta

	RStudio addins and R functions that make copy-pasting vectors and tables to text painless.
	"""
	
	homepage = "https://github.com/milesmcbain/datapasta"
	cran = "datapasta" 

	version("3.1.0", md5="f1b5e17d8bd08ad1facc267bbbbe1dc2")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-readr@1.2:", type=("build", "run"))
	depends_on("r-clipr@0.3:", type=("build", "run"))
	depends_on("r-rstudioapi@0.6:", type=("build", "run"))
