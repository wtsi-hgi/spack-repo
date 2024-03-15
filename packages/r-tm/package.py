# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTm(RPackage):
	"""Text Mining Package

	A framework for text mining applications within R.
	"""
	
	homepage = "https://tm.r-forge.r-project.org/"
	cran = "tm" 

	version("0.7-12", md5="60d60d1df2964cedeccddf60eccd66e4")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-nlp@0.2.0:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-slam@0.1.37:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
