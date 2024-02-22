# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REmon(RPackage):
	"""Tools for Environmental and Ecological Survey Design

	Statistical tools for environmental and ecological surveys.
    Simulation-based power and precision analysis; detection probabilities from
    different survey designs; visual fast count estimation.
	"""
	
	cran = "emon" 

	version("1.3.2", md5="bc8f7a253e83ce63611228e955d86606")

	depends_on("r-mgcv", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
