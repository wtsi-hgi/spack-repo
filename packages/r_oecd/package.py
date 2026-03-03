# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROecd(RPackage):
	"""Search and Extract Data from the OECD

	Search and extract data from the Organization for Economic 
    Cooperation and Development (OECD).
	"""
	
	homepage = "https://github.com/expersso/OECD"
	cran = "OECD" 

	version("0.2.5", md5="9a3ca27942197ee6886aa610a7f9f14c")

	depends_on("r-httr@0.6.1:", type=("build", "run"))
	depends_on("r-readsdmx@0.3:", type=("build", "run"))
	depends_on("r-xml2@0.1.2:", type=("build", "run"))
