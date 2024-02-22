# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBibliometrixdata(RPackage):
	"""Bibliometrix Example Datasets

	It contains some example datasets used in 'bibliometrix'. The data are bibliographic datasets exported from the 'SCOPUS' (<https://scopus.com>) and 'Clarivate Analytics Web of Science' (<https://www.webofscience.com/>) databases. They can be used to test the different features of the package 'bibliometrix' (<https://bibliometrix.org>). 
	"""
	
	cran = "bibliometrixData" 

	version("0.3.0", md5="a6fb49b014528060bc78b598e6d66402")

	depends_on("r@3.3:", type=("build", "run"))
