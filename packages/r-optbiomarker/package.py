# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROptbiomarker(RPackage):
	"""Estimation of Optimal Number of Biomarkers for Two-Group
Microarray Based Classifications at a Given Error Tolerance
Level for Various Classification Rules

	Estimates optimal number of biomarkers for two-group
        classification based on microarray data.
	"""
	
	cran = "optBiomarker" 

	version("1.0-28", md5="6110d8aa6fc1dc7dbb12aefae93917b1")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-rpanel", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ipred", type=("build", "run"))
	depends_on("r-msm", type=("build", "run"))
	depends_on("r-rgl", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
