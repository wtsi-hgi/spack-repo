# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexreg(RPackage):
	"""Conversion of R Regression Output to LaTeX or HTML Tables

	Converts coefficients, standard errors, significance stars, and goodness-of-fit statistics of statistical models into LaTeX tables or HTML tables/MS Word documents or to nicely formatted screen output for the R console for easy model comparison. A list of several models can be combined in a single table. The output is highly customizable. New model types can be easily implemented. Details can be found in Leifeld (2013), JStatSoft <doi:10.18637/jss.v055.i08>. (If the Zelig package, which this package enhances, cannot be found on CRAN, you can find it at <https://github.com/IQSS/Zelig>. If the mnlogit package, which this package enhances, cannot be found on CRAN, you can find an old version in the CRAN Archive at <https://cran.r-project.org/src/contrib/Archive/mnlogit/>.)
	"""
	
	homepage = "https://github.com/leifeld/texreg/"
	cran = "texreg" 

	version("1.39.3", md5="d1b3d675c10e8c148367810d5a15e005")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("pandoc@1.12.3:", type=("build", "link", "run"))
