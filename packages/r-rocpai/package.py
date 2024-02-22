# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRocpai(RPackage):
	"""Receiver Operating Characteristic Partial Area Indexes for evaluating classifiers

	The package analyzes the Curve ROC, identificates it among different types of Curve ROC and calculates the area under de curve through the method that is most accuracy. This package is able to standarizate proper and improper pAUC.
	"""
	
	bioc = "ROCpAI" 
	urls = ["https://www.bioconductor.org/packages/release/bioc/src/contrib/ROCpAI_1.14.0.tar.gz", "https://www.bioconductor.org/packages/release/bioc/src/contrib/Archive/ROCpAI/ROCpAI_1.14.0.tar.gz"]

	version("1.14.0", md5="8d2702c4029efeb23248e107384ffd27")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-fission", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
