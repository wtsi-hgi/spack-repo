# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatabaseconnectorjars(RPackage):
	"""JAR Dependencies for the 'DatabaseConnector' Package

	Provides external JAR dependencies for the 'DatabaseConnector' package.
	"""
	
	homepage = "https://github.com/OHDSI/DatabaseConnectorJars"
	cran = "DatabaseConnectorJars" 

	version("1.1.0", md5="d6734405723810913116c40b9655949f")

	depends_on("r-rjava", type=("build", "run"))
