# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPoisbinordnonnor(RPackage):
	"""Generation of Up to Four Different Types of Variables

	Generation of a chosen number of count, binary, ordinal, and continuous random variables, with specified correlations and marginal properties. The details of the method are explained in Demirtas (2012) <DOI:10.1002/sim.5362>.
	"""
	
	cran = "PoisBinOrdNonNor" 

	version("1.5.3", md5="c756d80a23348ee4074d8cbfb8bb36f2")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-corpcor", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-genord", type=("build", "run"))
	depends_on("r-bb", type=("build", "run"))
