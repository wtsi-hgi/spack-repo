# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCauphy(RPackage):
	"""Trait Evolution on Phylogenies Using the Cauchy Process

	The Cauchy Process can model pulsed continuous trait evolution
    on phylogenies. The likelihood is tractable, and is used for parameter
    inference and ancestral trait reconstruction.
    See Bastide and Didier (2023) <doi:10.1093/sysbio/syad053>.
	"""
	
	homepage = "https://gilles-didier.github.io/cauphy/"
	cran = "cauphy" 

	version("1.0.2", md5="8fde9814b9a126a1cc4202ce79424f6f")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ape@5.5:", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-phylolm", type=("build", "run"))
	depends_on("r-nloptr", type=("build", "run"))
	depends_on("r-pracma", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-hdinterval", type=("build", "run"))
