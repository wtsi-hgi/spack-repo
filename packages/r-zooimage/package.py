# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RZooimage(RPackage):
	"""Analysis of Numerical Plankton Images

	A free (open source) solution for analyzing digital
  images of plankton. In combination with ImageJ, a free image analysis
  system, it processes digital images, measures individuals, trains for
  automatic classification of taxa, and finally, measures plankton samples
  (abundances, total and partial size spectra or biomasses, etc.).
	"""
	
	homepage = "http://www.sciviews.org/zooimage"
	cran = "zooimage" 

	version("5.5.2", md5="a2bdb871bb94ea9c863a47b677ff13ad")

	depends_on("r@2.15:", type=("build", "run"))
	depends_on("r-mlearning", type=("build", "run"))
	depends_on("r-svmisc@0.9.67:", type=("build", "run"))
	depends_on("r-svdialogs@0.9.53:", type=("build", "run"))
	depends_on("r-filehash", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-mda", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-dt", type=("build", "run"))
