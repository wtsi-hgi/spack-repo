# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RKfda(RPackage):
	"""Kernel Fisher Discriminant Analysis

	Kernel Fisher Discriminant Analysis (KFDA) is performed using Kernel Principal Component Analysis (KPCA) and Fisher Discriminant Analysis (FDA).
    There are some similar packages. First, 'lfda' is a package that performs Local Fisher Discriminant Analysis (LFDA) and performs other functions.
    In particular, 'lfda' seems to be impossible to test because it needs the label information of the data in the function argument. Also, the 'ks' package has a limited dimension, which makes it difficult to analyze properly.
    This package is a simple and practical package for KFDA based on the paper of Yang, J., Jin, Z., Yang, J. Y., Zhang, D., and Frangi, A. F. (2004) <DOI:10.1016/j.patcog.2003.10.015>.
	"""
	
	homepage = "https://github.com/ainsuotain/kfda"
	cran = "kfda" 

	version("1.0.0", md5="8568c66bc460ccd359f6d21e834ae198")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
