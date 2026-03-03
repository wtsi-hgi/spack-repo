# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDppack(RPackage):
	"""Differentially Private Statistical Analysis and Machine Learning

	An implementation of common statistical analysis and models with
    differential privacy (Dwork et al., 2006a) <doi:10.1007/11681878_14>
    guarantees. The package contains, for example, functions providing
    differentially private computations of mean, variance, median, histograms,
    and contingency tables. It also implements some statistical models and
    machine learning algorithms such as linear regression (Kifer et al., 2012)
    <https://proceedings.mlr.press/v23/kifer12.html>
    and SVM (Chaudhuri et al., 2011)
    <https://jmlr.org/papers/v12/chaudhuri11a.html>. In addition, it implements
    some popular randomization mechanisms
    such as the Laplace mechanism (Dwork et al., 2006a)
    <doi:10.1007/11681878_14>, Gaussian mechanism (Dwork et al., 2006b)
    <doi:10.1007/11761679_29>, and exponential mechanism
    (McSherry & Talwar, 2007) <doi:10.1109/FOCS.2007.66>.
	"""
	
	cran = "DPpack" 

	version("0.1.0", md5="df1031cc38fa675fe850c41c4d7222c6")

	depends_on("r-rmutil@1.1.5:", type=("build", "run"))
	depends_on("r-rdpack@2.1.2:", type=("build", "run"))
	depends_on("r-r6@2.5.1:", type=("build", "run"))
	depends_on("r-dplyr@1.0.1:", type=("build", "run"))
	depends_on("r-mass@7.3.51.6:", type=("build", "run"))
	depends_on("r-nloptr@1.2.2.2:", type=("build", "run"))
	depends_on("r-e1071@1.7.9:", type=("build", "run"))
	depends_on("r-ggplot2@3.3.2:", type=("build", "run"))
