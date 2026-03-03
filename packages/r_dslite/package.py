# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDslite(RPackage):
	"""'DataSHIELD' Implementation on Local Datasets

	'DataSHIELD' is an infrastructure and series of R packages that 
    enables the remote and 'non-disclosive' analysis of sensitive research data.
    This 'DataSHIELD Interface' implementation is for analyzing datasets living
    in the current R session. The purpose of this is primarily for lightweight
    'DataSHIELD' analysis package development.
	"""
	
	homepage = "https://github.com/datashield/DSLite/"
	cran = "DSLite" 

	version("1.4.0", md5="d0a9281393c6f2efa79cf96958f99f71")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-dsi@1.5:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rly", type=("build", "run"))
