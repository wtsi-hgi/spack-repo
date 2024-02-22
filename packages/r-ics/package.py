# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcs(RPackage):
	"""Tools for Exploring Multivariate Data via ICS/ICA

	Implementation of Tyler, Critchley, Duembgen and Oja's (JRSS B, 2009,
            <doi:10.1111/j.1467-9868.2009.00706.x>) and Oja, Sirkia and Eriksson's
            (AJS, 2006, <https://www.ajs.or.at/index.php/ajs/article/view/vol35,%20no2%263%20-%207>) method of two different
            scatter matrices to obtain an invariant coordinate system or independent
            components, depending on the underlying assumptions. 
	"""
	
	cran = "ICS" 

	version("1.4-1", md5="73b4e57b9c43534ffd8e44d0b0ddd239")

	depends_on("r@2.5:", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
	depends_on("r-survey", type=("build", "run"))
