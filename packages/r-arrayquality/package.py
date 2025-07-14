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

    version("1.86.0", tag="RELEASE_3_21")
	version("1.80.0", sha256="3fb865babf7e0c400638556ddd475a05d0a7c6960a2f445073270656dc37a4ae")

	depends_on("r@2.2:", type=("build", "run"))
	depends_on("r-gridbase", type=("build", "run"))
	depends_on("r-hexbin", type=("build", "run"))
	depends_on("r-limma", type=("build", "run"))
	depends_on("r-marray", type=("build", "run"))
	depends_on("r-rcolorbrewer", type=("build", "run"))
