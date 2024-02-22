# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNucim(RPackage):
	"""Nucleome Imaging Toolbox

	
    Tools for 4D nucleome imaging. 
    Quantitative analysis of the 3D nuclear landscape recorded with super-resolved fluorescence microscopy. 
    See Volker J. Schmid, Marion Cremer, Thomas Cremer (2017) <doi:10.1016/j.ymeth.2017.03.013>.
	"""
	
	homepage = "https://bioimaginggroup.github.io/nucim/"
	cran = "nucim" 

	version("1.0.11", md5="f3dc2e46da63d7aa6610d23611d40715")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-ebimage", type=("build", "run"))
	depends_on("r-bioimagetools@1.1.4:", type=("build", "run"))
	depends_on("r-fields", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
	depends_on("fftw", type=("build", "link", "run"))
	depends_on("curl", type=("build", "link", "run"))
	depends_on("openssl", type=("build", "link", "run"))
