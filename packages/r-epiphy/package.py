# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REpiphy(RPackage):
	"""Analysis of Plant Disease Epidemics

	A toolbox to make it easy to analyze plant disease epidemics. It
    provides a common framework for plant disease intensity data recorded over
    time and/or space. Implemented statistical methods are currently mainly
    focused on spatial pattern analysis (e.g., aggregation indices, Taylor and
    binary power laws, distribution fitting, SADIE and 'mapcomp' methods). See
    Laurence V. Madden, Gareth Hughes, Franck van den Bosch (2007)
    <doi:10.1094/9780890545058> for further information on these methods.
    Several data sets that were mainly published in plant disease epidemiology
    literature are also included in this package.
	"""
	
	homepage = "https://github.com/chgigot/epiphy"
	cran = "epiphy" 

	version("0.5.0", md5="a41122d03bc4808ba64873740b2b17cd")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-transport", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
