# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDsi(RPackage):
	"""'DataSHIELD' Interface

	'DataSHIELD' is an infrastructure and series of R packages that 
    enables the remote and 'non-disclosive' analysis of sensitive research data. 
    This package defines the API that is to be implemented by 'DataSHIELD' compliant 
    data repositories.
	"""
	
	homepage = "https://github.com/datashield/DSI/"
	cran = "DSI" 

	version("1.5.0", md5="c132a6ef444c33dc9037bac4e164f277")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
