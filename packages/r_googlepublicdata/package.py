# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGooglepublicdata(RPackage):
	"""Working with Google's 'Public Data Explorer' DSPL Metadata Files

	Provides a collection of functions to set up 'Google Public Data Explorer'
  <https://www.google.com/publicdata/> data visualization tool with your own data,
  building automatically the corresponding DataSet Publishing Language file, or
  DSPL (XML), metadata file jointly with the CSV files. All zip-up and ready to
  be published in 'Public Data Explorer'.
	"""
	
	homepage = "http://github.com/gvegayon/googlePublicData/"
	cran = "googlePublicData" 

	version("0.16.1", md5="7358f9025886bc51ecdf415df127162d")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-xml", type=("build", "run"))
	depends_on("r-readxl", type=("build", "run"))
