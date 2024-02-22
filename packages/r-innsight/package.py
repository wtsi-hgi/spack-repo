# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RInnsight(RPackage):
	"""Get the Insights of Your Neural Network

	Interpretation methods for analyzing the behavior and individual
    predictions of modern neural networks in a three-step procedure: Converting 
    the model, running the interpretation method, and visualizing the results. 
    Implemented methods are, e.g., 'Connection Weights' described by Olden et al. (2004)
    <doi:10.1016/j.ecolmodel.2004.03.013>, layer-wise relevance
    propagation ('LRP') described by Bach et al. (2015)
    <doi:10.1371/journal.pone.0130140>, deep learning important features
    ('DeepLIFT') described by Shrikumar et al.  (2017) <arXiv:1704.02685>
    and gradient-based methods like 'SmoothGrad' described by Smilkov et
    al. (2017) <arXiv:1706.03825>, 'Gradient x Input' described by
    Baehrens et al. (2009) <arXiv:0912.1128> or 'Vanilla Gradient'.
	"""
	
	homepage = "https://bips-hb.github.io/innsight/"
	cran = "innsight" 

	version("0.3.0", md5="8b4aecdb713ab11727237b57ddea23ac")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-cli", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-torch", type=("build", "run"))
