# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCregg(RPackage):
	"""Simple Conjoint Tidying, Analysis, and Visualization

	Simple tidying, analysis, and visualization of conjoint (factorial) experiments, including estimation and visualization of average marginal component effects ('AMCEs') and marginal means ('MMs') for weighted and un-weighted survey data, along with useful reference category diagnostics and statistical tests. Estimation of 'AMCEs' is based upon methods described by Hainmueller, Hopkins, and Yamamoto (2014) <doi:10.1093/pan/mpt024>.
	"""
	
	homepage = "https://github.com/leeper/cregg"
	cran = "cregg" 

	version("0.4.0", md5="d99d95161a5bc5fcc4a49ca171977655")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-sandwich@2.4.0:", type=("build", "run"))
	depends_on("r-survey@3.33:", type=("build", "run"))
	depends_on("r-lmtest", type=("build", "run"))
	depends_on("r-ggplot2@2:", type=("build", "run"))
	depends_on("r-ggstance", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
