# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBootwar(RPackage):
	"""Nonparametric Bootstrap Test with Pooled Resampling Card Game

	The card game War is simple in its rules but can be lengthy. In
    another domain, the nonparametric bootstrap test with pooled resampling
    (nbpr) methods, as outlined in Dwivedi, Mallawaarachchi, and Alvarado (2017) <doi:10.1002/sim.7263>,
    is optimal for comparing paired or unpaired means in non-normal data,
    especially for small sample size studies. However, many researchers are
    unfamiliar with these methods. The 'bootwar' package bridges this gap by
    enabling users to grasp the concepts of nbpr via Boot War, a variation of the
    card game War designed for small samples. The package provides functions like
    score_keeper() and play_round() to streamline gameplay and scoring. Once a
    predetermined number of rounds concludes, users can employ the analyze_game()
    function to derive game results. This function leverages the 'npboottprm'
    package's nonparboot() to report nbpr results and, for comparative analysis,
    also reports results from the 'stats' package's t.test() function. Additionally,
    'bootwar' features an interactive 'shiny' web application, bootwar(). This
    offers a user-centric interface to experience Boot War, enhancing understanding
    of nbpr methods across various distributions, sample sizes, number of bootstrap
    resamples, and confidence intervals.
	"""
	
	homepage = "https://github.com/mightymetrika/bootwar"
	cran = "bootwar" 

	version("0.2.1", md5="4674675d1a9ca75e22d71340ad1df171")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mmcards", type=("build", "run"))
	depends_on("r-npboottprm", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-shinyjs", type=("build", "run"))
	depends_on("r-shinythemes", type=("build", "run"))
