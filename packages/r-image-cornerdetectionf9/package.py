# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RImageCornerdetectionf9(RPackage):
	"""Find Corners in Digital Images with FAST-9

	An implementation of the "FAST-9" corner detection algorithm explained in the paper 'FASTER and better: A machine learning approach to corner detection' by Rosten E., Porter R. and Drummond T. (2008), available at <arXiv:0810.2434>.
    The package allows to detect corners in digital images.
	"""
	
	homepage = "https://github.com/bnosac/image"
	cran = "image.CornerDetectionF9" 

	version("0.1.0", md5="722e2f9596536b3aae2adfd25bddf55a", url="https://cran.r-project.org/src/contrib/image.CornerDetectionF9_0.1.0.tar.gz")

	depends_on("r-rcpp", type=("build", "run"))
