# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFamos(RPackage):
	"""A Flexible Algorithm for Model Selection

	Given a set of parameters describing model dynamics and a corresponding cost function,
    FAMoS performs a dynamic forward-backward model selection on a specified selection
    criterion. It also applies a non-local swap search method. Works on any cost function. 
    For detailed information see Gabel et al. (2019) <doi:10.1371/journal.pcbi.1007230>.
	"""
	
	cran = "FAMoS" 

	version("0.3.0", md5="31c3b59cb4dc31cf439aff728fc205ee")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-future", type=("build", "run"))
	depends_on("r-r-utils", type=("build", "run"))
