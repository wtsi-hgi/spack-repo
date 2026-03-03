# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RQcmetrics(RPackage):
	"""A Framework for Quality Control

	The package provides a framework for generic quality control of data. It permits to create, manage and visualise individual or sets of quality control metrics and generate quality control reports in various formats.
	"""
	
	homepage = "http://lgatto.github.io/qcmetrics/articles/qcmetrics.html"
	bioc = "qcmetrics" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/qcmetrics_1.40.1.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/qcmetrics/qcmetrics_1.40.1.tar.gz"]

	version("1.40.1", md5="909e62b8c2d23a07e083f04e734ef61b")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-biobase", type=("build", "run"))
	depends_on("r-knitr", type=("build", "run"))
	depends_on("r-xtable", type=("build", "run"))
	depends_on("r-pander", type=("build", "run"))
	depends_on("r-s4vectors", type=("build", "run"))
