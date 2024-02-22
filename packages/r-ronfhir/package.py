# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRonfhir(RPackage):
	"""Read and Search Interface to the 'HL7 FHIR' REST API

	R on FHIR is an easy to use wrapper around the 'HL7 FHIR' REST API (STU 3 and R4). It provides tools to easily read and search resources on a FHIR server and brings the results into the R environment. R on FHIR is based on the FhirClient of the official 'HL7 FHIR .NET API', also made by Firely.
	"""
	
	cran = "RonFHIR" 

	version("0.4.0", md5="753a74be7a5f2cdee8ef64ce50ec40ac")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
