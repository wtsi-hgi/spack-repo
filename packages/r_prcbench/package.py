# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPrcbench(RPackage):
	"""Testing Workbench for Precision-Recall Curves

	A testing workbench to evaluate tools that calculate precision-recall curves.
    Saito and Rehmsmeier (2015) <doi:10.1371/journal.pone.0118432>.
	"""
	
	homepage = "https://evalclass.github.io/prcbench/"
	cran = "prcbench" 

	version("1.1.8", md5="8931c7e448d998a5ce47382c43385ed4")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6@2.1.1:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
	depends_on("r-gridextra@2:", type=("build", "run"))
	depends_on("r-ggplot2@2.1:", type=("build", "run"))
	depends_on("r-memoise@1:", type=("build", "run"))
	depends_on("r-rocr@1.0.7:", type=("build", "run"))
	depends_on("r-prroc@1.1:", type=("build", "run"))
	depends_on("r-precrec@0.1:", type=("build", "run"))
