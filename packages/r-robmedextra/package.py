# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRobmedextra(RPackage):
	"""Extra Functionality for (Robust) Mediation Analysis

	This companion package extends the package 'robmed' (Alfons, Ates & Groenen, 2022b; <doi:10.18637/jss.v103.i13>) in various ways.  Most notably, it provides a graphical user interface for the robust bootstrap test ROBMED (Alfons, Ates & Groenen, 2022a; <doi:10.1177/1094428121999096>) to make the method more accessible to less proficient 'R' users, as well as functions to export the results as a table in a 'Microsoft Word' or 'Microsoft Powerpoint' document, or as a 'LaTeX' table. Furthermore, the package contains a 'shiny' app to compare various bootstrap procedures for mediation analysis on simulated data.
	"""
	
	homepage = "https://github.com/aalfons/robmedExtra"
	cran = "robmedExtra" 

	version("0.1.0", md5="3afb557fc7f9a17faa49c114f963adce")

	depends_on("r-robmed@0.10:", type=("build", "run"))
	depends_on("r-shiny@1.1:", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
	depends_on("r-flextable@0.8.3:", type=("build", "run"))
	depends_on("r-ggplot2@3.3:", type=("build", "run"))
	depends_on("r-officer", type=("build", "run"))
