# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBioimagetools(RPackage):
	"""Tools for Microscopy Imaging

	Tools for 3D imaging, mostly for biology/microscopy. 
    Read and write TIFF stacks. Functions for segmentation, filtering and analyzing 3D point patterns.
	"""
	
	homepage = "https://bioimaginggroup.github.io/bioimagetools/"
	cran = "bioimagetools" 

	version("1.1.8", md5="b771a0c639d4edf95e80de3c8926bf54")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("fftw", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("openssl", type=("build", "link", "run"))
