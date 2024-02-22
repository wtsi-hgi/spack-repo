# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStatcodelists(RPackage):
	"""Use Standardized Statistical Codelists

	The goal of statcodelists is to promote the reuse and exchange of statistical 
    information and related metadata with making the internationally standardized SDMX code 
    lists available for the R user. SDMX has been published as an ISO International Standard 
    (ISO 17369). The metadata definitions, including the codelists are updated regularly 
    according to the standard. The authoritative version of the code lists made available in this
    package is <https://sdmx.org/?page_id=3215/>.
	"""
	
	homepage = "https://statcodelists.dataobservatory.eu"
	cran = "statcodelists" 

	version("0.9.2", md5="212546beb986d425498d7fedf75a1482")

	depends_on("r@2.10:", type=("build", "run"))
