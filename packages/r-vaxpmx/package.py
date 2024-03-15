# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RVaxpmx(RPackage):
	"""Vaccines Pharmacometrics

	Estimate vaccine efficacy (VE) using immunogenicity data.
    The inclusion of immunogenicity data in regression models can increase precision in VE. 
    The methods are described in the publication "Elucidating vaccine efficacy using a correlate of protection, demographics, and logistic regression" by Julie Dudasova, Zdenek Valenta, and Jeffrey R. Sachs (2024).
	"""
	
	cran = "vaxpmx" 

	version("0.0.3", md5="e326954f5dc673d3628cf4c915c32c0b")

	depends_on("r@4:", type=("build", "run"))
	depends_on("r-mass@7.3.51.6:", type=("build", "run"))
	depends_on("r-dplyr@1:", type=("build", "run"))
