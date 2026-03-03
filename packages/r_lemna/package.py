# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLemna(RPackage):
	"""Lemna Ecotox Effect Model

	The reference implementation of model equations and default
    parameters for the toxicokinetic-toxicodynamic (TKTD) model of the Lemna
    (duckweed) aquatic plant. Lemna is a standard test macrophyte used in ecotox
    effect studies. The model was described and published by the SETAC Europe
    Interest Group Effect Modeling. It is a refined description of the Lemna
    TKTD model published by Schmitt et al. (2013)
    <doi:10.1016/j.ecolmodel.2013.01.017>.
	"""
	
	homepage = "https://github.com/nkehrein/lemna"
	cran = "lemna" 

	version("1.0.1", md5="bfc9e8cdfb3c079f66dbe66521eea32b")

	depends_on("r@3.60:", type=("build", "run"))
	depends_on("r-desolve", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-gridextra", type=("build", "run"))
