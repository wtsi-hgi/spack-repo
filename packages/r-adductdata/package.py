# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdductdata(RPackage):
	"""Data from untargeted MS of modifications to Cys34 of serum albumin

	mzXML files from Grigoryan et al 2016 (Anal Chem).
	"""
	
	bioc = "adductData"

	version("1.24.0", commit="525af6152dcf5ac91c10a88b0b78bafb7b80e32f")
	version("1.18.0", commit="b94004e21edf65fb22a7e80459d4a0e4fcae296d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-experimenthub@1.9:", type=("build", "run"))
	depends_on("r-annotationhub@2.13.10:", type=("build", "run"))

