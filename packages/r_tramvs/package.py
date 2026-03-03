# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTramvs(RPackage):
	"""Optimal Subset Selection for Transformation Models

	Greedy optimal subset selection for transformation models 
    (Hothorn et al., 2018, <doi:10.1111/sjos.12291> ) based on the abess
    algorithm (Zhu et al., 2020, <doi:10.1073/pnas.2014241117> ). Applicable to
    models from packages 'tram' and 'cotram'.
	"""
	
	homepage = "http://ctm.R-forge.R-project.org"
	cran = "tramvs" 

	version("0.0-4", md5="3fc3dd21e9c6c7bd875cf22c517e9316")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-tram@0.6.1:", type=("build", "run"))
	depends_on("r-variables", type=("build", "run"))
	depends_on("r-cotram", type=("build", "run"))
