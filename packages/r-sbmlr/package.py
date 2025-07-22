# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSbmlr(RPackage):
	"""SBML-R Interface and Analysis Tools

	This package contains a systems biology markup language (SBML) interface to R.
	"""
	
	homepage = "http://epbi-radivot.cwru.edu/SBMLR/SBMLR.html"
	bioc = "SBMLR" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/SBMLR_1.98.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/SBMLR/SBMLR_1.98.0.tar.gz"]

	version("1.98.0", sha256="2abcd86c8baac8cea1698a321cb996dea62909b7407cadc793343bfef2cf90b2")

	depends_on("r-xml", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
