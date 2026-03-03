# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwitchselection(RPackage):
	"""Endogenous Switching and Sample Selection Regression Models

	Estimate the parameters of multivariate endogenous switching and sample selection models using methods described in Newey (2009) <doi:10.1111/j.1368-423X.2008.00263.x>, E. Kossova, B. Potanin (2018) <https://ideas.repec.org/a/ris/apltrx/0346.html>, E. Kossova, L. Kupriianova, B. Potanin (2020) <https://ideas.repec.org/a/ris/apltrx/0391.html> and E. Kossova, B. Potanin (2022) <https://ideas.repec.org/a/ris/apltrx/0455.html>. 
	"""
	
	cran = "switchSelection" 

	version("1.1.2", md5="5c400241dab1bbd4378699b5336fc964")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-hpa", type=("build", "run"))
	depends_on("r-mnorm", type=("build", "run"))
	depends_on("r-gena@1:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
