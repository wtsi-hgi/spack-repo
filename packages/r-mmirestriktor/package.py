# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMmirestriktor(RPackage):
	"""Informative Hypothesis Testing Web Applications

	Offering enhanced statistical power compared to traditional
    hypothesis testing methods, informative hypothesis testing allows researchers
    to explicitly model their expectations regarding the relationships among
    parameters. An important software tool for this framework is 'restriktor'.
    The 'mmirestriktor' package provides 'shiny' web applications to implement
    some of the basic functionality of 'restriktor'. The mmirestriktor() function
    launches a 'shiny' application for fitting and analyzing models with
    constraints. The FbarCards() function launches a card game application which
    can help build intuition about informative hypothesis testing. The
    iht_interpreter() helps interpret informative hypothesis testing results based
    on guidelines in Vanbrabant and Rosseel (2020) <doi:10.4324/9780429273872-14>.
	"""
	
	homepage = "https://github.com/mightymetrika/mmirestriktor"
	cran = "mmirestriktor" 

	version("0.2.1", md5="1931196b4a33e1ca9dc05a9a250951f6")

	depends_on("r-dt", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mmcards", type=("build", "run"))
	depends_on("r-restriktor", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
