# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGets(RPackage):
	"""General-to-Specific (GETS) Modelling and Indicator Saturation
Methods

	Automated General-to-Specific (GETS) modelling of the mean and variance of a regression, and indicator saturation methods for detecting and testing for structural breaks in the mean, see Pretis, Reade and Sucarrat (2018) <doi:10.18637/jss.v086.i03>.
	"""
	
	homepage = "https://CRAN.R-project.org/package=gets"
	cran = "gets" 

	version("0.37", md5="4aa37654fbb6978fa75927c07e84293a")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
