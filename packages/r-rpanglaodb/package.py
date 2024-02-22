# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRpanglaodb(RPackage):
	"""Download and Merge Single-Cell RNA-Seq Data from the PanglaoDB
Database

	Download and merge labeled single-cell RNA-seq data from the PanglaoDB <https://panglaodb.se/> into a Seurat object.
	"""
	
	homepage = "https://github.com/dosorio/rPanglaoDB/"
	cran = "rPanglaoDB" 

	version("0.2.1", md5="54ee881d83f8972364e1200f5440531f")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-seurat", type=("build", "run"))
	depends_on("r-pbapply", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
