# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGoogleknowledgegraphr(RPackage):
	"""Retrieve Information from 'Google Knowledge Graph' API

	Allows you to retrieve information from the 'Google Knowledge Graph' API <https://www.google.com/intl/bn/insidesearch/features/search/knowledge.html> and process it in R in various forms. The 'Knowledge Graph Search' API lets you find entities in the 'Google Knowledge Graph'. The API uses standard 'schema.org' types and is compliant with the 'JSON-LD' specification.
	"""
	
	cran = "GoogleKnowledgeGraphR" 

	version("0.1.0", md5="f479b42bab7472a40604beb365768c8c")

	depends_on("r-jsonlite", type=("build", "run"))
	depends_on("r-curl", type=("build", "run"))
