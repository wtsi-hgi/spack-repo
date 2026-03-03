# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROaiharvester(RPackage):
	"""Harvest Metadata Using OAI-PMH Version 2.0

	
  Harvest metadata using the Open Archives Initiative Protocol for Metadata
  Harvesting (OAI-PMH) version 2.0 (for more information, see
  <https://www.openarchives.org/OAI/openarchivesprotocol.html>).
	"""
	
	cran = "OAIHarvester" 

	version("0.3-4", md5="7b959b4bf194526044aefbe21fd6c00b")

	depends_on("r-curl", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
