# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RReadoffice(RPackage):
	"""Read Text Out of Modern Office Files

	Reads in text from 'unstructured' modern Microsoft Office files (XML based files) such as Word and PowerPoint.
    This does not read in structured data (from Excel or Access) as there are many other great packages to that do so already.
	"""
	
	cran = "readOffice" 

	version("0.2.2", md5="350a48734c1b1e5905c9faad73da1f41")

	depends_on("r-xml2@1:", type=("build", "run"))
	depends_on("r-rvest@0.3.2:", type=("build", "run"))
	depends_on("r-purrr@0.2.2:", type=("build", "run"))
	depends_on("r-magrittr@1.5:", type=("build", "run"))
