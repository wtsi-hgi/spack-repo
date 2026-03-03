# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlyingr(RPackage):
	"""Simulation of Bird Flight Range

	Functions for range estimation in birds based on Pennycuick (2008)
    and Pennycuick (1975), 'Flight' program which compliments Pennycuick (2008)
    requires manual entry of birds which can be tedious when there are hundreds
    of birds to estimate. Implemented are two ODE methods discussed in Pennycuick (1975)
    and time-marching computation methods as in Pennycuick (1998) and Pennycuick (2008).
    See Pennycuick (1975, ISBN:978-0-12-249405-5), Pennycuick (1998) <doi:10.1006/jtbi.1997.0572>,
    and Pennycuick (2008, ISBN:9780080557816).
	"""
	
	homepage = "https://github.com/BMasinde/FlyingR"
	cran = "FlyingR" 

	version("0.2.2", md5="22a9de9bb772ba0608c9955c23bcd142")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-kableextra", type=("build", "run"))
	depends_on("r-rmarkdown", type=("build", "run"))
