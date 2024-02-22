# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJaspar2016(RPackage):
	"""Data package for JASPAR 2016

	Data package for JASPAR 2016. To search this databases, please use the package TFBSTools (>= 1.8.1).
	"""
	
	homepage = "http://jaspar.genereg.net/"
	bioc = "JASPAR2016" 
	urls = ["https://www.bioconductor.org/packages/release/data/experiment/src/contrib/JASPAR2016_1.30.0.tar.gz", "https://www.bioconductor.org/packages/release/data/experiment/src/contrib/Archive/JASPAR2016/JASPAR2016_1.30.0.tar.gz"]

	version("1.30.0", md5="2976e4678291944f664396385049180b", url="https://www.bioconductor.org/packages/release/data/experiment/src/contrib/JASPAR2016_1.30.0.tar.gz")

	depends_on("r@3.2.2:", type=("build", "run"))

	# experiment