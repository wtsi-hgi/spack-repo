# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxode2random(RPackage):
	"""Random Number Generation Functions for 'rxode2'

	Provides the random number generation (in parallel) needed for
   'rxode2' (Wang, Hallow and  James (2016) <doi:10.1002/psp4.12052>) and 'nlmixr2'
    (Fidler et al (2019) <doi:10.1002/psp4.12445>).
    This split will reduce computational burden of recompiling 'rxode2'.
	"""
	
	homepage = "https://nlmixr2.github.io/rxode2random/"
	cran = "rxode2random" 

	version("2.0.13", md5="14c758530f611c1df169228fdc8abcd7")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-lotri", type=("build", "run"))
	depends_on("r-rxode2parse@2.0.17:", type=("build", "run"))
	depends_on("r-sitmo", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
