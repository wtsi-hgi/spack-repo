# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWnominate(RPackage):
	"""Roll Call Analysis Software

	Estimates Poole and Rosenthal's (1985 <doi:10.2307/2111172>, 1991 <doi:10.2307/2111445>)
	W-NOMINATE scores from roll call votes supplied though a 'rollcall'
	object from the 'pscl' package.
	"""
	
	cran = "wnominate" 

	version("1.4", md5="3f21d032d578795cc7320a33aa6e5e2f")

	depends_on("r@2.3.1:", type=("build", "run"))
	depends_on("r-pscl@0.59:", type=("build", "run"))
