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
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/SIM_1.72.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/SIM/SIM_1.72.0.tar.gz"]

	version("1.72.0", md5="72c2ca38244f4d53842bece2abdfadee")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-quantreg", type=("build", "run"))
	depends_on("r-globaltest", type=("build", "run"))
	depends_on("r-quantsmooth", type=("build", "run"))
