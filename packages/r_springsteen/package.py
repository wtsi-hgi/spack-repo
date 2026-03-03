# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSpringsteen(RPackage):
	"""All Things Data and Springsteen

	An R data package containing setlists from all Bruce Springsteen concerts over 1973-2021. 
    Also includes all his song details such as lyrics and albums. Data extracted from: 
    <http://brucebase.wikidot.com/>.
	"""
	
	homepage = "https://github.com/obrienjoey/spRingsteen"
	cran = "spRingsteen" 

	version("0.1.0", md5="6f9f67329328ba66956967a25e59b4cc")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-devtools", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
