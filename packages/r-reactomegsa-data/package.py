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
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/ReactomeGSA.data_1.16.1.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/ReactomeGSA.data/ReactomeGSA.data_1.16.1.tar.gz"]

	version("1.16.1", sha256="23aef32a3c97e44dcf88463efec0255e341ffe655f5238ccdee6bf452dd4c4a2")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-edger", type=("build", "run"))
	depends_on("r-reactomegsa", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))

