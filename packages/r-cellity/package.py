# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCellity(RPackage):
	"""Quality Control for Single-Cell RNA-seq Data

	A support vector machine approach to identifying and filtering low quality cells from single-cell RNA-seq datasets.
	"""
	
	bioc = "cellity" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/cellity_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/cellity/cellity_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="65d16d34707036da175a98e8f83346709e13bd150cb1342ccdf87136921bacf1")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-annotationdbi", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-mvoutlier", type=("build", "run"))
	depends_on("r-org-hs-eg-db", type=("build", "run"))
	depends_on("r-org-mm-eg-db", type=("build", "run"))
	depends_on("r-robustbase", type=("build", "run"))
	depends_on("r-topgo", type=("build", "run"))
