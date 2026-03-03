# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmPluginEuropresse(RPackage):
	"""Import Articles from 'Europresse' Using the 'tm' Text Mining
Framework

	Provides a 'tm' Source to create corpora from
  articles exported from the 'Europresse' content provider as
  HTML files. It is able to read both text content and meta-data
  information (including source, date, title, author and pages).
	"""
	
	homepage = "https://r-forge.r-project.org/projects/r-temis/"
	cran = "tm.plugin.europresse" 

	version("1.4", md5="c86b3fd957b0fa8167347a8949b0ba24")

	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-tm@0.6:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
