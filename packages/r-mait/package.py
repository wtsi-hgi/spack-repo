# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMait(RPackage):
	"""Statistical Analysis of Metabolomic Data

	The MAIT package contains functions to perform end-to-end statistical analysis of LC/MS Metabolomic Data. Special emphasis is put on peak annotation and in modular function design of the functions.
	"""
	
	bioc = "MAIT" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/MAIT_1.36.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/MAIT/MAIT_1.36.0.tar.gz"]

    version("1.42.0", tag="RELEASE_3_21")
	version("1.36.0", sha256="cfc0d04449641e29cd782659b47f23ae4148e37f6a4a5cc64aadb65f41e192ce")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-camera", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-gplots", type=("build", "run"))
	depends_on("r-e1071", type=("build", "run"))
	depends_on("r-class", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-plsgenomics", type=("build", "run"))
	depends_on("r-agricolae", type=("build", "run"))
	depends_on("r-xcms", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
