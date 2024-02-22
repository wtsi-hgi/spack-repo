# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIrtoys(RPackage):
	"""A Collection of Functions Related to Item Response Theory (IRT)

	A collection of functions useful in learning and practicing IRT,
    which can be combined into larger programs. Provides basic CTT analysis,
    a simple common interface to the estimation of item
    parameters in IRT models for binary responses with three different programs
    (ICL, BILOG-MG, and ltm), ability estimation (MLE, BME, EAP, WLE, plausible 
    values), item and person fit statistics, scaling methods (MM, MS, Stocking-Lord,
    and the complete Hebaera method), and a rich array of parametric and 
    non-parametric (kernel) plots. Estimates and plots Haberman's interaction model
    when all items are dichotomously scored.
	"""
	
	cran = "irtoys" 

	version("0.2.2", md5="0366e3f53467f935ff3f77ca5814400e")

	depends_on("r-sm", type=("build", "run"))
	depends_on("r-ltm", type=("build", "run"))
