# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAffixcan(RPackage):
	"""A Functional Approach To Impute Genetically Regulated Expression

	Impute a GReX (Genetically Regulated Expression) for a set of genes in a sample of individuals, using a method based on the Total Binding Affinity (TBA). Statistical models to impute GReX can be trained with a training dataset where the real total expression values are known.
	"""
	
	bioc = "AffiXcan"

	version("1.26.0", commit="80538fc7269b1ce9515fb76342e4bd04cca24ea4")
	version("1.20.0", commit="26a1df70634d281287a41122c7dfdd873d79dd9d")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
