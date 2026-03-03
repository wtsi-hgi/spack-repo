# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLatex2exp(RPackage):
	"""Use LaTeX Expressions in Plots

	Parses and converts LaTeX math formulas to R's plotmath
    expressions, used to enter mathematical formulas and symbols to be rendered as
    text, axis labels, etc. throughout R's plotting system.
	"""
	
	homepage = "https://www.stefanom.io/latex2exp/"
	cran = "latex2exp" 

	version("0.9.6", md5="cd7516e9f3f56ef6720e4107016f5931")

	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
