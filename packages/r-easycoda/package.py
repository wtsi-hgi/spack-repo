# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REasycoda(RPackage):
	"""Compositional Data Analysis in Practice

	Univariate and multivariate methods for compositional data 
    analysis, based on logratios. The package implements the approach in the
    book Compositional Data Analysis in Practice by Michael Greenacre (2018),
    where accent is given to simple pairwise logratios. Selection can be made
    of logratios that account for a maximum percentage of logratio variance.
    Various multivariate analyses of logratios are included in the package. 
	"""
	
	homepage = "https://github.com/michaelgreenacre/CODAinPractice/"
	cran = "easyCODA" 

	version("0.34.3", md5="71794a23da6227f269d20c0453515d76")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-ca@0.7:", type=("build", "run"))
	depends_on("r-vegan@2.3:", type=("build", "run"))
	depends_on("r-ellipse@0.4.1:", type=("build", "run"))
