# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2020(RPackage):
	"""Data package for JASPAR database (version 2020)

	Data package for JASPAR2020. To search this databases, please use the package TFBSTools (>= 1.23.1).
	"""
	
	homepage = "http://jaspar.genereg.net/"
	bioc = "JASPAR2020" 
	urls = ["https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/JASPAR2020_0.99.10.tar.gz", "https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/Archive/JASPAR2020/JASPAR2020_0.99.10.tar.gz"]

	version("0.99.10", md5="bfcaf41ebf0935b8d146afd37719de2d", url="https://www.bioconductor.org/packages/3.18/data/annotation/src/contrib/JASPAR2020_0.99.10.tar.gz")

	depends_on("r@3.6:", type=("build", "run"))

