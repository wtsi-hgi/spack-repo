# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSignacx(RPackage):
	"""Cell Type Identification and Discovery from Single Cell Gene
Expression Data

	An implementation of neural networks trained with flow-sorted gene expression data to classify cellular phenotypes in single cell RNA-sequencing data. See Chamberlain M et al. (2021) <doi:10.1101/2021.02.01.429207> for more details.
	"""
	
	homepage = "https://github.com/mathewchamberlain/SignacX"
	cran = "SignacX" 

	version("2.2.5", md5="02af63c99fd123f11c9f6f5bed682b07")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-neuralnet", type=("build", "run"))
	depends_on("r-lme4", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-pbmcapply", type=("build", "run"))
	depends_on("r-seurat@3.2:", type=("build", "run"))
	depends_on("r-rjsonio", type=("build", "run"))
	depends_on("r-igraph@1.2.1:", type=("build", "run"))
	depends_on("r-jsonlite@1.5:", type=("build", "run"))
	depends_on("r-rcolorbrewer@1.1.2:", type=("build", "run"))
