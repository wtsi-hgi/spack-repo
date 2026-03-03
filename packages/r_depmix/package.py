# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDepmix(RPackage):
	"""Dependent Mixture Models

	Fits (multigroup) mixtures of latent or hidden Markov models on mixed categorical and continuous (timeseries) data. The 'Rdonlp2' package can optionally be used for optimization of the log-likelihood and is available from R-forge. See Visser et al. (2009, <DOI:10.1007/978-0-387-95922-1_13>) for examples and applications. 
	"""
	
	cran = "depmix" 

	version("0.9.16", md5="479d0971bcffb1000193e3f8afeab8a7")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
