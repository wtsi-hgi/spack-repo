# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRquantlib(RPackage):
	"""R Interface to the 'QuantLib' Library

	The 'RQuantLib' package makes parts of 'QuantLib' accessible from R
 The 'QuantLib' project aims to provide a comprehensive software framework
 for quantitative finance. The goal is to provide a standard open source library
 for quantitative analysis, modeling, trading, and risk management of financial
 assets.
	"""
	
	homepage = "https://github.com/eddelbuettel/rquantlib"
	cran = "RQuantLib" 

	version("0.4.21", md5="954b47a29afd7d2e08c27fa445c6b61a")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("quantlib@1.14:", type=("build", "link", "run"))
	depends_on("boost", type=("build", "link", "run"))
