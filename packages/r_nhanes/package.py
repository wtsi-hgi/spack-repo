# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNhanes(RPackage):
	"""Data from the US National Health and Nutrition Examination Study

	Body Shape and related measurements from the US National Health
    and Nutrition Examination Survey (NHANES, 1999-2004).  See
    http://www.cdc.gov/nchs/nhanes.htm for details.
	"""
	
	cran = "NHANES" 

	version("2.1.0", md5="1ea2bd012219f856ebe80b0c5d91d64a")

	depends_on("r@3:", type=("build", "run"))
