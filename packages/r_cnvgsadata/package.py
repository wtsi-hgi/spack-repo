# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCnvgsadata(RPackage):
	"""Data used in the vignette of the cnvGSA package

	This package contains the data used in the vignette of the cnvGSA package.
	"""
	
	bioc = "cnvGSAdata" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/cnvGSAdata_1.38.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/cnvGSAdata/cnvGSAdata_1.38.0.tar.gz"]

	version("1.38.0", md5="1cc86a2066cae55493d710c475cc7112")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cnvgsa", type=("build", "run"))

