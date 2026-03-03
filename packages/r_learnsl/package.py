# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLearnsl(RPackage):
	"""Learn Supervised Classification Methods Through Examples and
Code

	Supervised classification methods, which (if asked) can provide
    step-by-step explanations of the algorithms used, as described in
    PK Josephine et. al., (2021) <doi:10.59176/kjcs.v1i1.1259>; and datasets to
    test them on, which highlight the strengths and weaknesses of each technique.
	"""
	
	homepage = "https://github.com/ComiSeng/LearnSL"
	cran = "LearnSL" 

	version("1.0.0", md5="c42be1cb0ba27d700192ac2d37b524cf")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-cli@3.6.1:", type=("build", "run"))
