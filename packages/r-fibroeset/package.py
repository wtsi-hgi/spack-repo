# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFibroeset(RPackage):
	"""exprSet for Karaman et al. (2003) fibroblasts data

	exprSet for Karaman et al. (2003) human, bonobo and gorilla fibroblasts data
	"""
	
	bioc = "fibroEset" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/fibroEset_1.44.0.tar.gz", "https://www.bioconductor.org/packages/3.18/data/experiment/src/contrib/Archive/fibroEset/fibroEset_1.44.0.tar.gz"]

	version("1.44.0", sha256="86a4364b0615e992820a78056b6f70798544f471368e492fdf563f279fb9bf9d")

	depends_on("r-biobase@2.5.5:", type=("build", "run"))

