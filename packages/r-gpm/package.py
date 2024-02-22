# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGpm(RPackage):
	"""Gaussian Process Modeling of Multi-Response and Possibly Noisy
Datasets

	Provides a general and efficient tool for fitting a response surface to a dataset via Gaussian processes. The dataset can have multiple responses and be noisy (with stationary variance). The fitted GP model can predict the gradient as well. The package is based on the work of Bostanabad, R., Kearney, T., Tao, S. Y., Apley, D. W. & Chen, W. (2018) Leveraging the nugget parameter for efficient Gaussian process modeling. International Journal for Numerical Methods in Engineering, 114, 501-516.
	"""
	
	cran = "GPM" 

	version("3.0.1", md5="805537302830224f70deed6d495de51c")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-lhs@0.14:", type=("build", "run"))
	depends_on("r-randtoolbox@1.17:", type=("build", "run"))
	depends_on("r-lattice@0.20.34:", type=("build", "run"))
	depends_on("r-pracma@2.1.8:", type=("build", "run"))
	depends_on("r-foreach@1.4.4:", type=("build", "run"))
	depends_on("r-doparallel@1.0.14:", type=("build", "run"))
	depends_on("r-iterators@1.0.10:", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
