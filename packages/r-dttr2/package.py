# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDttr2(RPackage):
	"""Manipulate Date, POSIXct and hms Vectors

	Manipulates date ('Date'), date time ('POSIXct') and time
    ('hms') vectors.  Date/times are considered discrete and are floored
    whenever encountered.  Times are wrapped and time zones are maintained
    unless explicitly altered by the user.
	"""
	
	homepage = "https://github.com/poissonconsulting/dttr2"
	cran = "dttr2" 

	version("0.5.0", md5="81f158c4ae785cdbb30be23967ed2dcb", url="https://cran.r-project.org/src/contrib/dttr2_0.5.0.tar.gz")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-chk@0.9.1:", type=("build", "run"))
	depends_on("r-hms", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
