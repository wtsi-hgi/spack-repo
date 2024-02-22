# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROpenimager(RPackage):
	"""An Image Processing Toolkit

	Incorporates functions for image preprocessing, filtering and image recognition. The package takes advantage of 'RcppArmadillo' to speed up computationally intensive functions. The histogram of oriented gradients descriptor is a modification of the 'findHOGFeatures' function of the 'SimpleCV' computer vision platform, the average_hash(), dhash() and phash() functions are based on the 'ImageHash' python library. The Gabor Feature Extraction functions are based on 'Matlab' code of the paper, "CloudID: Trustworthy cloud-based and cross-enterprise biometric identification" by M. Haghighat, S. Zonouz, M. Abdel-Mottaleb, Expert Systems with Applications, vol. 42, no. 21, pp. 7905-7916, 2015, <doi:10.1016/j.eswa.2015.06.025>. The 'SLIC' and 'SLICO' superpixel algorithms were explained in detail in (i) "SLIC Superpixels Compared to State-of-the-art Superpixel Methods", Radhakrishna Achanta, Appu Shaji, Kevin Smith, Aurelien Lucchi, Pascal Fua, and Sabine Suesstrunk, IEEE Transactions on Pattern Analysis and Machine Intelligence, vol. 34, num. 11, p. 2274-2282, May 2012, <doi:10.1109/TPAMI.2012.120> and (ii) "SLIC Superpixels", Radhakrishna Achanta, Appu Shaji, Kevin Smith, Aurelien Lucchi, Pascal Fua, and Sabine Suesstrunk, EPFL Technical Report no. 149300, June 2010.
	"""
	
	homepage = "https://github.com/mlampros/OpenImageR"
	cran = "OpenImageR" 

	version("1.3.0", md5="dc4ae6886635637b4f3fcbfdd7a0133f")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-shiny", type=("build", "run"))
	depends_on("r-jpeg", type=("build", "run"))
	depends_on("r-png", type=("build", "run"))
	depends_on("r-tiff", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.8:", type=("build", "run"))
	depends_on("armadillo", type=("build", "link", "run"))
	depends_on("lapack", type=("build", "link", "run"))
	depends_on("arpack", type=("build", "link", "run"))
	depends_on("gcc", type=("build", "link", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))
	depends_on("libpng", type=("build", "link", "run"))
	depends_on("fftw@3:", type=("build", "link", "run"))
	depends_on("libtiff", type=("build", "link", "run"))
