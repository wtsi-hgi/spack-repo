# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFscaret(RPackage):
	"""Automated Feature Selection from 'caret'

	Automated feature selection using variety of models
        provided by 'caret' package.
        This work was funded by Poland-Singapore bilateral cooperation
        project no 2/3/POL-SIN/2012.
	"""
	
	cran = "fscaret" 

	version("0.9.4.4", md5="b81f841a2f37752862f2884317cc108e")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-caret", type=("build", "run"))
	depends_on("r-gsubfn", type=("build", "run"))
	depends_on("r-hmeasure", type=("build", "run"))
