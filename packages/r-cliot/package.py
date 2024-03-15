# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliot(RPackage):
	"""Clinical Indices and Outcomes Tools

	Collection of indices and tools relating to cardiovascular, nephrology, and hepatic research that aid epidemiological chort or retrospective chart review with big data. All indices and tools take commonly used lab values and patient demographics and measurements to compute various risk and predictive values for survival. References to original literature and validation contained in each function documentation.
	"""
	
	cran = "cliot" 

	version("0.2.0", md5="01d3a982749a96f6aabf1b7ff16a78bd")

