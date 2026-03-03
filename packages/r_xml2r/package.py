# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RXml2r(RPackage):
	"""EasieR XML data collection

	XML2R is a framework that reduces the effort required to transform
    XML content into number of tables while preserving parent to child
    relationships.
	"""
	
	homepage = "http://cpsievert.github.com/XML2R"
	cran = "XML2R" 

	version("0.0.6", md5="2c9f9d3870f9b54c7d89fe9212aee921")

	depends_on("r@2.15.1:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
