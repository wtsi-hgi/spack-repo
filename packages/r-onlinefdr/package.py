# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROnlinefdr(RPackage):
	"""Online error rate control

	This package allows users to control the false discovery rate (FDR) or familywise error rate (FWER) for online multiple hypothesis testing, where hypotheses arrive in a stream. In this framework, a null hypothesis is rejected based on the evidence against it and on the previous rejection decisions.
	"""
	
	homepage = "https://dsrobertson.github.io/onlineFDR/index.html"
	bioc = "onlineFDR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/onlineFDR_2.10.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/onlineFDR/onlineFDR_2.10.0.tar.gz"]

	version("2.10.0", sha256="f5f14f3b7ec8b936778cdbfd505b01248be0b786d9ff8c3afd1c5605f93db80d")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
