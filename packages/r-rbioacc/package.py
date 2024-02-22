# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRbioacc(RPackage):
	"""Inference and Prediction of ToxicoKinetic (TK) Models

	The MOSAICbioacc application is a turnkey package providing bioaccumulation
    factors (BCF/BMF/BSAF) from a toxicokinetic (TK) model fitted to
    accumulation-depuration data. It is designed to fulfil the requirements
    of regulators when examining applications for market authorization of active
    substances. See Ratier et al. (2021) <doi:10.1101/2021.09.08.459421>.
	"""
	
	homepage = "https://gitlab.com/qonfluens/model/rbioacc"
	cran = "rbioacc" 

	version("1.2-0", md5="b8590cb1258b7cf1ca57f7260a8138bf")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-rstan@2.26:", type=("build", "run"))
	depends_on("r-rstantools@2.1.1:", type=("build", "run"))
	depends_on("r-ggmcmc", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-loo", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-zoo", type=("build", "run"))
	depends_on("r-bh@1.66:", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.3.3:", type=("build", "run"))
	depends_on("r-rcppparallel@5.0.1:", type=("build", "run"))
	depends_on("r-stanheaders@2.26:", type=("build", "run"))
