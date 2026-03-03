# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmPluginDc(RPackage):
	"""Text Mining Distributed Corpus Plug-in

	A plug-in for the text mining framework tm to support text mining 
             in a distributed way. The package provides a convenient interface for
             handling distributed corpus objects based on distributed list objects.
	"""
	
	cran = "tm.plugin.dc" 

	version("0.2-10", md5="f7d45c0eea7905a6d967fc73347a17b1")

	depends_on("r-dsl@0.1.7:", type=("build", "run"))
	depends_on("r-tm@0.7:", type=("build", "run"))
	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-slam@0.1.22:", type=("build", "run"))
