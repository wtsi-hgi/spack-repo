# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdmiralTest(RPackage):
	"""Test Data for the 'admiral' Package

	A set of Study Data Tabulation Model (SDTM) datasets from the Clinical
    Data Interchange Standards Consortium (CDISC) pilot project used for testing
    and developing Analysis Data Model (ADaM) derivations inside the 'admiral'
    package.
	"""
	
	cran = "admiral.test" 

	version("0.7.0", md5="ba429cee7c4e9188f1958358f8e93edd")

	depends_on("r@3.5:", type=("build", "run"))
