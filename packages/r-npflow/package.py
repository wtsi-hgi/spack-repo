# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNpflow(RPackage):
	"""Bayesian Nonparametrics for Automatic Gating of Flow-Cytometry
Data

	Dirichlet process mixture of multivariate normal, skew normal or skew t-distributions
             modeling oriented towards flow-cytometry data preprocessing applications. Method is 
             detailed in: Hejblum, Alkhassimn, Gottardo, Caron & Thiebaut (2019) <doi: 10.1214/18-AOAS1209>.
	"""
	
	cran = "NPflow" 

	version("0.13.5", md5="dbadc3edf4e43a6db68356dfebb9961c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-truncnorm", type=("build", "run"))
	depends_on("r-ellipse", type=("build", "run"))
	depends_on("r-fastcluster", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-pheatmap", type=("build", "run"))
	depends_on("r-reshape2", type=("build", "run"))
	depends_on("r-ggally", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
