# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTmPluginAlceste(RPackage):
	"""Import texts from files in the Alceste format using the tm text
mining framework

	This package provides a tm Source to create corpora from
  a corpus prepared in the format used by the Alceste application (i.e.
  a single text file with inline meta-data). It is able to import both
  text contents and meta-data (starred) variables.
	"""
	
	homepage = "https://r-forge.r-project.org/projects/r-temis/"
	cran = "tm.plugin.alceste" 

	version("1.1", md5="7118fe140a1c3c51c12ed409ec4741c8")

	depends_on("r-nlp", type=("build", "run"))
	depends_on("r-tm@0.6:", type=("build", "run"))
