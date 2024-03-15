# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPathling(RPackage):
	"""A Library for using 'Pathling'

	R API for 'Pathling', a tool for querying and transforming electronic health record data that is represented using the 'Fast Healthcare Interoperability Resources' (FHIR) standard - see <https://pathling.csiro.au/docs>.
	"""
	
	homepage = "https://pathling.csiro.au/"
	cran = "pathling" 

	version("6.4.2", md5="9fda04b262bb1ebcf3e9b7f8f1873071")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rlang@1:", type=("build", "run"))
	depends_on("r-sparklyr@1.8.4:", type=("build", "run"))
	depends_on("spark@3.4:", type=("build", "link", "run"))
