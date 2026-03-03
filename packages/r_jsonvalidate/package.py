# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJsonvalidate(RPackage):
	"""Validate 'JSON' Schema

	Uses the node library 'is-my-json-valid' or 'ajv' to
    validate 'JSON' against a 'JSON' schema.  Drafts 04, 06 and 07 of
    'JSON' schema are supported.
	"""
	
	homepage = "https://docs.ropensci.org/jsonvalidate/"
	cran = "jsonvalidate" 

	version("1.3.2", md5="aeb5c0cc44825e0a9a8a5678e7eb5fe2")

	depends_on("r-v8", type=("build", "run"))
