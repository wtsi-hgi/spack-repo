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

	version("1.8.0", commit="b2fba458dff22406b4ee6588419babfdf01f71c9")
	version("1.2.0", commit="d2128b2f4ca724d4e2dce2956618d185f0ffa0a0")

