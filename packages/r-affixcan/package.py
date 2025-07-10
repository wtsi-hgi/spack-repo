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
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/AffiXcan_1.20.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/AffiXcan/AffiXcan_1.20.0.tar.gz"]

	version("1.20.0", sha256="5930e4d789838200d4ee3d046b61178fea080915cdb32aeeaeb5ea5dbe46a0b8")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-multiassayexperiment", type=("build", "run"))
	depends_on("r-biocparallel", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
