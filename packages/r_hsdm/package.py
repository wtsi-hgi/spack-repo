# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHsdm(RPackage):
	"""Hierarchical Bayesian Species Distribution Models

	User-friendly and fast set of functions for estimating parameters of hierarchical Bayesian species distribution models (Latimer and others 2006 <doi:10.1890/04-0609>). Such models allow interpreting the observations (occurrence and abundance of a species) as a result of several hierarchical processes including ecological processes (habitat suitability, spatial dependence and anthropogenic disturbance) and observation processes (species detectability). Hierarchical species distribution models are essential for accurately characterizing the environmental response of species, predicting their probability of occurrence, and assessing uncertainty in the model results.
	"""
	
	homepage = "https://ecology.ghislainv.fr/hSDM/"
	cran = "hSDM" 

	version("1.4.4", md5="1911091eebf324393fcbf2aff3408d90")

	depends_on("r-coda", type=("build", "run"))
	depends_on("gsl", type=("build", "link", "run"))
