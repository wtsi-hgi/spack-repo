# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmPluginMail(RPackage):
	"""Text Mining E-Mail Plug-in

	A plug-in for the tm text mining framework providing mail handling
  functionality.
	"""
	
	cran = "tm.plugin.mail" 

	version("0.2-2", md5="08ee002d1eff1f6f417ed22d94e47cc9")

	depends_on("r-nlp@0.1.2:", type=("build", "run"))
	depends_on("r-tm@0.6.1:", type=("build", "run"))
