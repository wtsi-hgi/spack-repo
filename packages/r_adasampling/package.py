# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdasampling(RPackage):
	"""Adaptive Sampling for Positive Unlabeled and Label Noise
Learning

	Implements the adaptive sampling procedure, a framework for both positive unlabeled learning and learning with class label noise. Yang, P., Ormerod, J., Liu, W., Ma, C., Zomaya, A., Yang, J. (2018) <doi:10.1109/TCYB.2018.2816984>.
	"""
	
	homepage = "https://github.com/PengyiYang/AdaSampling/"
	cran = "AdaSampling" 

	version("1.3", md5="af4a7074c9bcc52fc232fc32bdbdfc0c")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-caret@6.0.78:", type=("build", "run"))
	depends_on("r-class@7.3.14:", type=("build", "run"))
	depends_on("r-e1071@1.6.8:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
