# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REvots(RPackage):
	"""Analyses of Evolutionary Time-Series

	Facilitates univariate and multivariate analysis of evolutionary sequences of phenotypic change. The package extends the modeling framework available in the 'paleoTS' package. Please see <https://klvoje.github.io/evoTS/index.html> for information about the package and the implemented models. 
	"""
	
	homepage = "https://klvoje.github.io/evoTS/index.html"
	cran = "evoTS" 

	version("1.0.2", md5="fefac76c2caa963974090e4c73fd8542")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-paleots@0.4.4:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-plotly", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
