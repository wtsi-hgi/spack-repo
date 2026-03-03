# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDundermifflin(RPackage):
	"""The Office Quotes on-Demand

	Provides functions to randomly select, return, and print
  quotes or entire scenes from the American version of
  the show the Office. Receive laughs from one of of the 
  greatest sitcoms of all time on demand. Add these functions 
  to your  '.Rprofile' to get a good laugh everytime you start
  a new R session.
	"""
	
	cran = "dundermifflin" 

	version("0.1.1", md5="575d5f1fc0aa9ea44669bebbc4446a16")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-stringi", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
