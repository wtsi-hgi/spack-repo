# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIgor(RPackage):
	"""Intergovernmental Organizations Database

	Tools to extract information from the Intergovernmental
    Organizations ('IGO') Database , version 3, provided by the Correlates
    of War Project <https://correlatesofwar.org/>. See also Pevehouse, J.
    C. et al. (2020).  Version 3 includes information from 1815 to 2014.
	"""
	
	homepage = "https://dieghernan.github.io/igoR/"
	cran = "igoR" 

	version("0.2.0", md5="93c2a964c889e858d276c1b762bc8b9b")

	depends_on("r@2.10:", type=("build", "run"))
