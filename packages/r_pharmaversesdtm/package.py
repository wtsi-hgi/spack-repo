# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPharmaversesdtm(RPackage):
	"""Test Data for the Pharmaverse Family of Packages

	A set of Study Data Tabulation Model (SDTM) datasets from the Clinical
    Data Interchange Standards Consortium (CDISC) pilot project used for testing
    and developing Analysis Data Model (ADaM) datasets inside the pharmaverse 
    family of packages. SDTM dataset specifications are described in: CDISC Submission Data Standards Team
    (2021) <https://www.cdisc.org/system/files/members/standard/foundational/SDTMIG%20v3.4-FINAL_2022-07-21.pdf>.
	"""
	
	homepage = "https://pharmaverse.github.io/pharmaversesdtm/main/"
	cran = "pharmaversesdtm" 

	version("0.2.0", md5="7f752328f8dfdd3813d3121943858be0")

	depends_on("r@3.5:", type=("build", "run"))
