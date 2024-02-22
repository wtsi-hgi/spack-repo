# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBloq(RPackage):
	"""Impute and Analyze Data with BLOQ Observations

	It includes estimating the area under the concentrations
        versus time curve (AUC) and its standard error for data with
        Below the Limit of Quantification (BLOQ) observations. Two 
        approaches are implemented: direct estimation using censored maximum 
        likelihood, also by first imputing the BLOQ's 
        using various methods, then compute AUC and its standard 
        error using imputed data. Technical details can found in 
        Barnett, Helen Yvette, Helena Geys, Tom Jacobs, and Thomas Jaki. 
		"Methods for Non-Compartmental Pharmacokinetic Analysis With Observations 
		Below the Limit of Quantification." Statistics in Biopharmaceutical 
		Research (2020): 1-12.
        (available online: 
        <https://www.tandfonline.com/doi/full/10.1080/19466315.2019.1701546>). 
	"""
	
	cran = "BLOQ" 

	version("0.1-1", md5="862e51b2571a285accd7fa453602ab46")

	depends_on("r-maxlik", type=("build", "run"))
	depends_on("r-mvtnorm", type=("build", "run"))
