# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAlabasterSchemas(RPackage):
	"""Schemas for the Alabaster Framework

	Stores all schemas required by various alabaster.* packages. No computation should be performed by this package, as that is handled by alabaster.base. We use a separate package instead of storing the schemas in alabaster.base itself, to avoid conflating management of the schemas with code maintenence.
	"""
	
	bioc = "alabaster.schemas" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/alabaster.schemas_1.2.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/alabaster.schemas/alabaster.schemas_1.2.0.tar.gz"]

	version("1.2.0", sha256="c1d74a8560654dcc4bf1254b39bc0e15938387038be9eec91daf1cd72569976b")

