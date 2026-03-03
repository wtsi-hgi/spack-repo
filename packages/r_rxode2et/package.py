# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxode2et(RPackage):
	"""Event Table Functions for 'rxode2'

	Provides the event table and support functions needed for
   'rxode2' (Wang, Hallow and  James (2016) <doi:10.1002/psp4.12052>) and 'nlmixr2'
    (Fidler et al (2019) <doi:10.1002/psp4.12445>).
    This split will reduce computational burden of recompiling 'rxode2'.
	"""
	
	homepage = "https://nlmixr2.github.io/rxode2et/"
	cran = "rxode2et" 

	version("2.0.12", md5="eb7c43d4208bb987b14c1cfda5ca1840")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rxode2random", type=("build", "run"))
	depends_on("r-rxode2parse", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-magrittr", type=("build", "run"))
	depends_on("r-lotri", type=("build", "run"))
