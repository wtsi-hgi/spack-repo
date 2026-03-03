# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDaime(RPackage):
	"""Effects of Changing Deposition Rates

	Reverse and model the effects of changing deposition rates on geological data and rates. Based on Hohmann (2018) <doi:10.13140/RG.2.2.23372.51841> .
	"""
	
	cran = "DAIME" 

	version("2.1.3", md5="6984dacfad157eee2863c89851135c96")

	depends_on("r@3.5:", type=("build", "run"))
