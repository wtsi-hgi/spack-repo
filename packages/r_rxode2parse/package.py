# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRxode2parse(RPackage):
	"""Parsing and Code Generation Functions for 'rxode2'

	Provides the parsing needed for 'rxode2' (Wang, Hallow and
    James (2016) <doi:10.1002/psp4.12052>). It also provides the 'stan'
    based advan linear compartment model solutions with gradients
    (Carpenter et al (2015), <arXiv:1509.07164>) needed in 'nlmixr2'
    (Fidler et al (2019) <doi:10.1002/psp4.12445>).
    This split will reduce computational burden of recompiling 'rxode2'.
	"""
	
	homepage = "https://nlmixr2.github.io/rxode2parse/"
	cran = "rxode2parse" 

	version("2.0.18", md5="9a564c91677dbe85a288dbb4fafcb17b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-dparser@1.3.1.10:", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-qs", type=("build", "run"))
	depends_on("r-rcpp@1.0.8:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-rex", type=("build", "run"))
	depends_on("r-symengine", type=("build", "run"))
	depends_on("r-data-table@1.12.4:", type=("build", "run"))
	depends_on("r-bh@1.78:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.9.2:", type=("build", "run"))
	depends_on("r-stanheaders@2.21.0.7:", type=("build", "run"))
