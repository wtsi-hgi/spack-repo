# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnviropra(RPackage):
	"""Environmental Probabilistic Risk Assessment Tools

	Methods to perform a Probabilistic Environmental Risk assessment from exposure to toxic substances - i.e. USEPA (1997) <https://www.epa.gov/risk/guiding-principles-monte-carlo-analysis> -.
	"""
	
	cran = "EnviroPRA" 

	version("1.0", md5="f7cf8b62ec029ef670864e1a48412831")

	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ksamples", type=("build", "run"))
	depends_on("r-fitdistrplus", type=("build", "run"))
	depends_on("r-truncdist", type=("build", "run"))
