# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRdiagnosislist(RPackage):
	"""Manipulate SNOMED CT Diagnosis Lists

	Functions and methods for manipulating 'SNOMED CT' concepts.
    The package contains functions for loading the 'SNOMED CT' release into
    a convenient R environment, selecting 'SNOMED CT' concepts using regular
    expressions, and navigating the 'SNOMED CT' ontology. It provides the
    'SNOMEDconcept' S3 class for a vector of 'SNOMED CT' concepts (stored
    as 64-bit integers) and the 'SNOMEDcodelist' S3 class for a table
    of concepts IDs with descriptions. For more information about 'SNOMED CT'
    visit <https://www.snomed.org/>.
	"""
	
	cran = "Rdiagnosislist" 

	version("1.2", md5="a64f9e922c5fa89344c9fc3342ac937b")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-bit64", type=("build", "run"))
