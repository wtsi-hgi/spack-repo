# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMetagxbreast(RPackage):
	"""Transcriptomic Breast Cancer Datasets

	A collection of Breast Cancer Transcriptomic Datasets that are part of the MetaGxData package compendium.
	"""
	
	bioc = "MetaGxBreast"

	version("1.28.0", commit="9e95d03f4548094c27aba4161439e72a26e336b9")
	version("1.22.0", commit="a3c220a01c313909d895bdd8f434be6c4f2a09fd")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-annotationhub", type=("build", "run"))
	depends_on("r-experimenthub", type=("build", "run"))
	depends_on("r-lattice", type=("build", "run"))
	depends_on("r-impute", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))

