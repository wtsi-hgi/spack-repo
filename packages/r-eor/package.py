# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REor(RPackage):
	"""Data Management Package (Exposure and Occurrence Data in R)

	This data management package provides some helper
    classes for publicly available data sources (HMD, DESTATIS) in
    Demography. Similar to ideas developed in the Bioconductor
    project <https://bioconductor.org> we strive to encapsulate data in easy
    to use S4 objects.
    If original data is provided in a text file, the resulting S4
    object contains all information from that text file. But the
    information is somehow structured (header, footer, etc).
    Further the classes provide methods to make a subset for selected
    calendar years or selected regions. The resulting subset
    objects still contain the original header and footer information.
	"""
	
	homepage = "https://github.molgen.mpg.de/walke/eoR"
	cran = "eoR" 

	version("0.4.0", md5="303d0486653009ea59365a5cc5e0a218")

	depends_on("r@3.2:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
