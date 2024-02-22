# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMulticastr(RPackage):
	"""A Companion to the Multi-CAST Collection

	Provides a basic interface for accessing annotation data from
   the Multi-CAST collection, a database of spoken natural language texts
   edited by Geoffrey Haig and Stefan Schnell. The collection draws from a
   diverse set of languages and has been annotated across multiple levels.
   Annotation data is downloaded on request from the servers of the
   University of Bamberg. See the Multi-CAST website
   <https://multicast.aspra.uni-bamberg.de/> for more information and a list
   of related publications.
	"""
	
	homepage = "https://multicast.aspra.uni-bamberg.de/"
	cran = "multicastR" 

	version("2.0.0", md5="b2c96b9ab1fcf4b7e0310147220d3420")

	depends_on("r@3:", type=("build", "run"))
