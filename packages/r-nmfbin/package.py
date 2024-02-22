# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNmfbin(RPackage):
	"""Non-Negative Matrix Factorization for Binary Data

	Factorize binary matrices into rank-k components using the logistic function in the updating process. See e.g. Tomé et al (2015) <doi:10.1007/s11045-013-0240-9> .
	"""
	
	homepage = "https://michalovadek.github.io/nmfbin/"
	cran = "nmfbin" 

	version("0.2.1", md5="399f28ebdc03f069ef9f8281a342b787")

