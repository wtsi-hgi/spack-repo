# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFurrowseg(RPackage):
	"""Furrow Segmentation

	Image feature data and analysis codes for the Guglielmi, Barry et al. paper describing the application of an optogenetics tools to disrupt Drosophila embryo furrowing.
	"""
	
	bioc = "furrowSeg"

	version("1.36.0", commit="65d9e3be51e01139f1d98e61cdb6643dfeef5621")
	version("1.30.0", commit="c435138f3dce0de0e454f1853a6bfb3ee9305811")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-locfit", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))

