# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAjv(RPackage):
	"""Another JSON Schema Validator

	A thin wrapper around the 'ajv' JSON validation package for
    JavaScript. See <http://epoberezkin.github.io/ajv/> for details.
	"""
	
	homepage = "https://github.com/jdthorpe/ajvr"
	cran = "ajv" 

	version("1.0.0", md5="6dc019c6beed4f27e576873cbe285a4b")

	depends_on("r-v8", type=("build", "run"))
	depends_on("r-yaml", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
