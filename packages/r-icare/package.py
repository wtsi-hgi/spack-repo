# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIcare(RPackage):
	"""A Tool for Individualized Coherent Absolute Risk Estimation (iCARE)

	An R package to compute Individualized Coherent Absolute Risk Estimators.
	"""
	
	bioc = "iCARE" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/iCARE_1.30.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/iCARE/iCARE_1.30.0.tar.gz"]

	version("1.36.0", tag="RELEASE_3_21")
	version("1.30.0", sha256="47e80ea396d8632601bb79caba8df0397df6564d84c6a51a43d1eb3fb91e0662")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-plotrix", type=("build", "run"))
	depends_on("r-gtools", type=("build", "run"))
	depends_on("r-hmisc", type=("build", "run"))
