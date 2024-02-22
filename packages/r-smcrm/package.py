# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSmcrm(RPackage):
	"""Data Sets for Statistical Methods in Customer Relationship
Management by Kumar and Petersen (2012)

	Data Sets for Kumar and Petersen (2012).
    Statistical Methods in Customer Relationship Management,
    Wiley: New York.
	"""
	
	cran = "SMCRM" 

	version("0.0-3", md5="03232e5c7ac002adb1c1beb59ffbeb50")

