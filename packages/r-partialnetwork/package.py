# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPartialnetwork(RPackage):
	"""Estimating Peer Effects Using Partial Network Data

	Implements IV-estimator and Bayesian estimator for linear-in-means Spatial Autoregressive (SAR) model (see LeSage, 1997 <doi:10.1177/016001769702000107>; Lee, 2004 <doi:10.1111/j.1468-0262.2004.00558.x>; Bramoullé et al., 2009 <doi:10.1016/j.jeconom.2008.12.021>), while assuming that only a partial information about the network structure is available. Examples are when the adjacency matrix is not fully observed or when only consistent estimation of the network formation model is available (see Boucher and Houndetoungan <https://ahoundetoungan.com/files/Papers/PartialNetwork.pdf>).
	"""
	
	homepage = "https://github.com/ahoundetoungan/PartialNetwork"
	cran = "PartialNetwork" 

	version("1.0.3", md5="be4254757216fd51a09dabbf01791cf0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-formula", type=("build", "run"))
	depends_on("r-formula-tools", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-matrix", type=("build", "run"))
	depends_on("r-doparallel", type=("build", "run"))
	depends_on("r-foreach", type=("build", "run"))
	depends_on("r-dorng", type=("build", "run"))
	depends_on("r-rcpparmadillo@0.11.4.4:", type=("build", "run"))
	depends_on("r-rcppeigen", type=("build", "run"))
	depends_on("r-rcppnumerical", type=("build", "run"))
	depends_on("r-rcppprogress", type=("build", "run"))
