# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSim(RPackage):
	"""Integrated Analysis on two human genomic datasets

	Finds associations between two human genomic datasets.
	"""
	
	bioc = "SIM" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SIM_1.72.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SIM/SIM_1.72.0.tar.gz"]

	version("1.72.0", sha256="d36d0744e2f24b175ee4f479b1deca86dc80d67eb1ea87c722e2723f563fec79")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-globaltest", type=("build", "run"))
	depends_on("r-quantsmooth", type=("build", "run"))
