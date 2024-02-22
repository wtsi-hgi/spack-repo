# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSimplace(RPackage):
	"""Interface to Use the Modelling Framework 'SIMPLACE'

	Interface to interact with the modelling framework 'SIMPLACE' and to
    parse the results of simulations.
	"""
	
	homepage = "https://github.com/gk-crop/simplace_rpkg/"
	cran = "simplace" 

	version("5.0.13", md5="1d4367e702e20a090a46e8b0c796461e")

	depends_on("r-rjava@0.9.13:", type=("build", "run"))
	depends_on("java@11:", type=("build", "link", "run"))
