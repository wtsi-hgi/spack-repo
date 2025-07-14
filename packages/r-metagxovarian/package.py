# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagxovarian(RPackage):
	"""Transcriptomic Ovarian Cancer Datasets

	A collection of Ovarian Cancer Transcriptomic Datasets that are part of the MetaGxData package compendium.
	"""
	
	bioc = "MetaGxOvarian"

	version("1.28.0", commit="0aa7c5c4360dc79ec9f8f84cacbc23bf50c8e323")
	version("1.22.0", commit="77bbd05732b91b46ea46c5166eb650a4dba852c3")

	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))

