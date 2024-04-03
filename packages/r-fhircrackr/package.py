# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFhircrackr(RPackage):
	"""Handling HL7 FHIR® Resources in R

	Useful tools for conveniently downloading FHIR resources in xml format 
    and converting them to R data.frames. The package uses FHIR-search to download bundles 
    from a FHIR server, provides functions to save and read xml-files containing such bundles 
    and allows flattening the bundles to data.frames using XPath expressions. FHIR® is the registered trademark 
    of HL7 and is used with the permission of HL7. Use of the FHIR trademark does not constitute endorsement of this product by HL7.
	"""
	
	cran = "fhircrackr" 

	version("2.1.1", md5="e43f64d31363b69aa257b281e32ce4c5")
	version("2.2.0", md5="e1ef831cfc78fc1a007a595304b4dea5")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
