# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRams(RPackage):
	"""R Access to Mass-Spec Data

	R-based access to mass-spectrometry (MS) data. While many packages 
  exist to process MS data, many of these make it difficult to 
  access the underlying mass-to-charge ratio (m/z), intensity, and 
  retention time of the files 
  themselves. This package is designed to format MS data in a tidy fashion and 
  allows the user perform the plotting and analysis.
	"""
	
	homepage = "https://github.com/wkumler/RaMS"
	cran = "RaMS" 

	version("1.4.0", md5="5b7efa340cf8ce21ec7e96dd09f97f4d")

	depends_on("r-xml2", type=("build", "run"))
	depends_on("r-base64enc", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
