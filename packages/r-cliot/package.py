# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCliot(RPackage):
	"""Clinical Indices and Outcomes Tools

	Collection of indices and tools relating to cardiovascular, nephrology, and hepatic research that aid epidemiological or retrospective review. All indices and tools take commonly used lab values and patient demographics and measurements to compute various risk and predictive values for survival. References to original literature and validation contained in each function documentation.
	"""
	
	cran = "cliot" 

	version("0.1.0", md5="f2246e0eea6a7ad2bc174dce1e89d577")

