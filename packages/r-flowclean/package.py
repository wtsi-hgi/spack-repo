# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowclean(RPackage):
	"""flowClean

	A quality control tool for flow cytometry data based on compositional data analysis.
	"""
	
	bioc = "flowClean" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/flowClean_1.40.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/flowClean/flowClean_1.40.0.tar.gz"]

	version("1.40.0", sha256="0a0029fd76fd2f9dd2ba7bd5ccabeeebb53438a947143e6bae79d96c55a00325")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-flowcore", type=("build", "run"))
	depends_on("r-bit", type=("build", "run"))
	depends_on("r-changepoint", type=("build", "run"))
	depends_on("r-sfsmisc", type=("build", "run"))
