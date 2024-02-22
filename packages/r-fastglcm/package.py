# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFastglcm(RPackage):
	"""'GLCM' Texture Features

	Two 'Gray Level Co-occurrence Matrix' ('GLCM') implementations are included: The first is a fast 'GLCM' feature texture computation based on 'Python' 'Numpy' arrays ('Github' Repository, <https://github.com/tzm030329/GLCM>). The second is a fast 'GLCM' 'RcppArmadillo' implementation which is parallelized (using 'OpenMP') with the option to return all 'GLCM' features at once. For more information, see "Artifact-Free Thin Cloud Removal Using Gans" by Toizumi Takahiro, Zini Simone, Sagi Kazutoshi, Kaneko Eiji, Tsukada Masato, Schettini Raimondo (2019), IEEE International Conference on Image Processing (ICIP), pp. 3596-3600, <doi:10.1109/ICIP.2019.8803652>.
	"""
	
	homepage = "https://github.com/mlampros/fastGLCM"
	cran = "fastGLCM" 

	version("1.0.2", md5="694645cc708e4ec82732531a37d6f4d5")

	depends_on("r@3.2.3:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-openimager", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
	depends_on("python@3:", type=("build", "link", "run"))
	depends_on("py-numpy", type=("build", "link", "run"))
	depends_on("opencv+python3", type=("build", "link", "run"))
	depends_on("py-matplotlib", type=("build", "link", "run"))
	depends_on("py-scikit-image", type=("build", "link", "run"))
	depends_on("armadillo", type=("build", "link", "run"))
	depends_on("blas", type=("build", "link", "run"))
	depends_on("lapack", type=("build", "link", "run"))
