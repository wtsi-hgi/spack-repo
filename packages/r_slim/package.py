# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSlim(RPackage):
	"""Singular Linear Models for Longitudinal Data

	Fits singular linear models to longitudinal data. Singular linear
    models are useful when the number, or timing, of longitudinal observations
    may be informative about the observations themselves. They are described
    in Farewell (2010) <doi:10.1093/biomet/asp068>, and are extensions of the
    linear increments model <doi:10.1111/j.1467-9876.2007.00590.x> to general
    longitudinal data.   
	"""
	
	cran = "slim" 

	version("0.1.1", md5="75b697bda68f6dad55741a8c381f43b5")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table@1.9.6:", type=("build", "run"))
	depends_on("r-mass@7.3:", type=("build", "run"))
