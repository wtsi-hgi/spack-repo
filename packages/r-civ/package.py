# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCiv(RPackage):
	"""Categorical Instrumental Variables

	Implementation of the categorical instrumental variable (CIV) 
    estimator proposed by Wiemann (2023) <arXiv:2311.17021>. CIV allows for optimal instrumental 
    variable estimation in settings with relatively few observations per 
    category. To obtain valid inference in these challenging settings, CIV
    leverages a regularization assumption that implies existence of a latent 
    categorical variable with fixed finite support achieving the same first 
    stage fit as the observed instrument.
	"""
	
	homepage = "https://github.com/thomaswiemann/civ"
	cran = "civ" 

	version("0.1.0", md5="de44355661ab6593ac466f9138ba96ce")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-aer", type=("build", "run"))
	depends_on("r-kcmeans", type=("build", "run"))
