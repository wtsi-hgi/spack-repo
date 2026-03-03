# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlatxml(RPackage):
	"""Tools for Working with XML Files as R Dataframes

	On import, the XML information is converted to a dataframe that reflects the hierarchical XML structure. Intuitive functions allow to navigate within this transparent XML data structure (without any knowledge of 'XPath'). 'flatXML' also provides tools to extract data from the XML into a flat dataframe that can be used to perform statistical operations. It also supports converting dataframes to XML.
	"""
	
	homepage = "https://github.com/jsugarelli/flatxml/"
	cran = "flatxml" 

	version("0.1.1", md5="d0fd41a013c29c04b5a17bc2e4cd7b57")

	depends_on("r-rcurl", type=("build", "run"))
	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
