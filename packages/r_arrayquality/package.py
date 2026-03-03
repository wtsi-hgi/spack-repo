# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RArrayquality(RPackage):
	"""Assessing array quality on spotted arrays

	Functions for performing print-run and array level quality assessment.
	"""
	
	homepage = "http://arrays.ucsf.edu/"
	bioc = "arrayQuality" 
	urls = ["https://www.bioconductor.org/packages/3.18/bioc/src/contrib/arrayQuality_1.80.0.tar.gz", "https://www.bioconductor.org/packages/3.18/bioc/src/contrib/Archive/arrayQuality/arrayQuality_1.80.0.tar.gz"]

	version("1.80.0", md5="9d875e31dc2f51e4c476d1a13330ad18")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
