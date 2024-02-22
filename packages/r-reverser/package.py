# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReverser(RPackage):
	"""Linear Regression Stability to Significance Reversal

	Tests linear regressions for significance reversal through leave-one(multiple)-out and shifting/addition of response values. The paradigm of the package is loosely based on the somewhat forgotten "dfstat" criterion (Belsley, Kuh & Welsch 1980 <doi:10.1002/0471725153.ch2>), which tests influential values in linear models from their effect on statistical inference, i.e. changes in p-value.
	"""
	
	cran = "reverseR" 

	version("0.1", md5="2a20b9648fc34f5af20e20ddea34ffb8")

	depends_on("r@2.13:", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-markdown", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
