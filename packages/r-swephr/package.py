# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSwephr(RPackage):
	"""High Precision Swiss Ephemeris

	The Swiss Ephemeris (version 2.10.03) is a high precision ephemeris based upon the
    DE431 ephemerides from NASA's JPL. It covers the time range 13201 BCE to
    17191 CE. This package uses the semi-analytic theory by Steve Moshier.
    For faster and more accurate calculations, the compressed Swiss Ephemeris
    data is available in the 'swephRdata' package. To access this data package,
    run 'install.packages("swephRdata", repos = "https://rstub.r-universe.dev",
    type = "source")'. The size of the 'swephRdata' package is approximately
    115 MB. The user can also use the original JPL DE431 data.
	"""
	
	homepage = "https://github.com/rstub/swephR/"
	cran = "swephR" 

	version("0.3.1", md5="b59d3655106a495f32e80dfdf458356e")

	depends_on("r-rcpp", type=("build", "run"))
