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

	version("2.10.0", md5="1fcb84d6fd99c3f48d43c07adc29f256")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
