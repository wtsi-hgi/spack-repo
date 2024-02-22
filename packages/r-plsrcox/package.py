# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPlsrcox(RPackage):
	"""Partial Least Squares Regression for Cox Models and Related
Techniques

	Provides Partial least squares Regression and various regular, sparse or kernel, techniques for fitting Cox models in high dimensional settings <doi:10.1093/bioinformatics/btu660>, Bastien, P., Bertrand, F., Meyer N., Maumy-Bertrand, M. (2015), Deviance residuals-based sparse PLS and sparse kernel PLS regression for censored data, Bioinformatics, 31(3):397-404. Cross validation criteria were studied in <arXiv:1810.02962>, Bertrand, F., Bastien, Ph. and Maumy-Bertrand, M. (2018), Cross validating extensions of kernel, sparse or regular partial least squares regression models to censored data.
	"""
	
	homepage = "http://fbertran.github.io/plsRcox/"
	cran = "plsRcox" 

	version("1.7.7", md5="f4ad0346e8bf1f04ddf7ba80739f0548")

	depends_on("r@2.4:", type=("build", "run"))
	depends_on("r-survival", type=("build", "run"))
	depends_on("r-plsrglm", type=("build", "run"))
	depends_on("r-lars", type=("build", "run"))
	depends_on("r-pls", type=("build", "run"))
	depends_on("r-kernlab", type=("build", "run"))
	depends_on("r-mixomics", type=("build", "run"))
	depends_on("r-risksetroc", type=("build", "run"))
	depends_on("r-survcomp", type=("build", "run"))
	depends_on("r-survauc", type=("build", "run"))
	depends_on("r-rms", type=("build", "run"))
