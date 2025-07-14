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

    version("1.44.0", tag="RELEASE_3_21")
	version("1.38.0", sha256="422d159ba3c4665196528a620853ce55663075b0265c7185e1589cd499995aa9")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-cnvgsa", type=("build", "run"))

