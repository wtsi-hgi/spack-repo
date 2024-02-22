# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLogicreg(RPackage):
	"""Logic Regression

	Routines for fitting Logic Regression models. Logic Regression is described
	in Ruczinski, Kooperberg, and LeBlanc (2003) <DOI:10.1198/1061860032238>. Monte
        Carlo Logic Regression is described in and Kooperberg and Ruczinski (2005)
        <DOI:10.1002/gepi.20042>.
	"""
	
	cran = "LogicReg" 

	version("1.6.6", md5="5719c33574524baed775d92c4588ddad")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
