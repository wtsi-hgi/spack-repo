# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMigrationIndices(RPackage):
	"""Migration Indices

	Calculate various indices, like Crude Migration Rate,
    different Gini indices or the Coefficient of Variation among others, to
    show the (un)equality of migration.
	"""
	
	homepage = "https://github.com/daroczig/migration.indices"
	cran = "migration.indices" 

	version("0.3.1", md5="572aa46c8cc566363840722d1ec432fd")

	depends_on("r-calibrate", type=("build", "run"))
