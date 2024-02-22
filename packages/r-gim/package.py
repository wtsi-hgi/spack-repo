# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGim(RPackage):
	"""Generalized Integration Model

	Implements the generalized integration model, which integrates individual-level data and summary statistics under a generalized linear model framework. It supports continuous and binary outcomes to be modeled by the linear and logistic regression models. For binary outcome, data can be sampled in prospective cohort studies or case-control studies. Described in Zhang et al. (2020)<doi:10.1093/biomet/asaa014>. 
	"""
	
	homepage = "https://github.com/zhangh12/gim"
	cran = "gim" 

	version("0.33.1", md5="5b943b9250bf78f70c13258323391bef")

	depends_on("r@3.4:", type=("build", "run"))
	depends_on("r-numderiv", type=("build", "run"))
