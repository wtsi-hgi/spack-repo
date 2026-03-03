# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLrmf3(RPackage):
	"""Low Rank Matrix Factorization S3 Objects

	Provides S3 classes to represent low rank matrix
    decompositions.
	"""
	
	homepage = "https://github.com/RoheLab/LRMF3"
	cran = "LRMF3" 

	version("0.1.0", md5="b5dfac08d1b010f878345342cf865424", url="https://cran.r-project.org/src/contrib/LRMF3_0.1.0.tar.gz")

	depends_on("r-matrix", type=("build", "run"))
	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
