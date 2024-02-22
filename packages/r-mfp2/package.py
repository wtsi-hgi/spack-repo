# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMfp2(RPackage):
	"""Multivariable Fractional Polynomial Models with Extensions

	Multivariable fractional polynomial algorithm simultaneously selects variables and functional forms in both generalized linear models and Cox proportional hazard models. Key references for this algorithm are Royston and Altman (1994)<doi:10.2307/2986270> and Sauerbrei and Royston (2008, ISBN:978-0-470-02842-1). In addition, it can model a 'sigmoid' relationship between variable x and an outcome variable y using the approximate cumulative distribution transformation proposed by Royston (2014) <doi:10.1177/1536867X1401400206>. This feature distinguishes it from a standard fractional polynomial function, which lacks the ability to achieve such modeling.
	"""
	
	homepage = "https://github.com/EdwinKipruto/mfp2"
	cran = "mfp2" 

	version("1.0.0", md5="bd17d1c4554a8a441cd3603b390bf2b7", url="https://cran.r-project.org/src/contrib/mfp2_1.0.0.tar.gz")

	depends_on("r@4.2:", type=("build", "run"))
	depends_on("r-ggplot2@3.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
