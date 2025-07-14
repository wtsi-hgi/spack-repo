# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReactomegsaData(RPackage):
	"""Companion data package for the ReactomeGSA package

	Companion data sets to showcase the functionality of the ReactomeGSA package. This package contains proteomics and RNA-seq data of the melanoma B-cell induction study by Griss et al. and scRNA-seq data from Jerby-Arnon et al.
	"""
	
	homepage = "https://github.com/reactome/ReactomeGSA.data/issues"
	bioc = "ReactomeGSA.data"

	version("1.22.0", commit="54a560d6532f0f9b28b64cea229a805d3a4ae350")
	version("1.16.1", commit="56f5b0b4479059163fd04005302f2bbb2ada9b9b")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-reactomegsa", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))

