# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGretaGp(RPackage):
	"""Gaussian Process Modelling in 'greta'

	Provides a syntax to create and combine Gaussian process kernels 
  in 'greta'. You can then them to define either full rank or sparse Gaussian 
  processes. This is an extension to the 'greta' software, Golding (2019) 
  <doi:10.21105/joss.01601>.
	"""
	
	homepage = "https://github.com/greta-dev/greta.gp"
	cran = "greta.gp" 

	version("0.2.1", md5="3deb1aad9237bc1e214f29ce99c2fa6c")

	depends_on("r-greta@0.4.2:", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
	depends_on("r-tensorflow@2.7:", type=("build", "run"))
	depends_on("python@2.7.0:", type=("build", "link", "run"))
	depends_on("py-tensorflow@1.14:", type=("build", "link", "run"))
	depends_on("py-tensorflow-probability", type=("build", "link", "run"))
