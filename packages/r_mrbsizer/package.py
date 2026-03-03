# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMrbsizer(RPackage):
	"""Scale Space Multiresolution Analysis of Random Signals

	A method for the multiresolution analysis of spatial fields and images to capture scale-dependent features.
    mrbsizeR is based on scale space smoothing and uses differences of smooths at neighbouring scales for finding features on different scales.
    To infer which of the captured features are credible, Bayesian analysis is used.
    The scale space multiresolution analysis has three steps: (1) Bayesian signal reconstruction.
    (2) Using differences of smooths, scale-dependent features of the reconstructed signal can be found.
    (3) Posterior credibility analysis of the differences of smooths created.
    The method has first been proposed by Holmstrom, Pasanen, Furrer, Sain (2011) <DOI:10.1016/j.csda.2011.04.011> and extended in Flury, Gerber, Schmid and Furrer (2021) <DOI:10.1016/j.spasta.2020.100483>.
	"""
	
	homepage = "https://github.com/romanflury/mrbsizeR"
	cran = "mrbsizeR" 

	version("1.3", md5="f08924440281d0f4ea50c6dd162c4929")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-maps@3.1.1:", type=("build", "run"))
	depends_on("r-fields@8.10:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
