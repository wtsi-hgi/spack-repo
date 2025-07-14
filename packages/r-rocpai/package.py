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

	version("1.20.0", commit="c3e65c9f2dc45e72da2fc31a81fd79a01b90bde3")
	version("1.14.0", commit="232b8e9a4a6ab699d79edf8416715ce451411a91")

	depends_on("r-boot", type=("build", "run"))
	depends_on("r-summarizedexperiment", type=("build", "run"))
	depends_on("r-fission", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
