# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDirect(RPackage):
	"""Bayesian Clustering of Multivariate Data Under the
Dirichlet-Process Prior

	A Bayesian clustering method for replicated time series or replicated measurements from multiple experimental conditions, e.g., time-course gene expression data.  It estimates the number of clusters directly from the data using a Dirichlet-process prior.  See Fu, A. Q., Russell, S., Bray, S. and Tavare, S. (2013) Bayesian clustering of replicated time-course gene expression data with weak signals. The Annals of Applied Statistics. 7(3) 1334-1361. <doi:10.1214/13-AOAS650>.
	"""
	
	cran = "DIRECT" 

	version("1.1.0", md5="3836df0a0a09e09cd9075386b60b75ab")

