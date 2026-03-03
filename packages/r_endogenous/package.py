# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REndogenous(RPackage):
	"""Classical Simultaneous Equation Models

	Likelihood-based approaches to estimate linear regression parameters and treatment effects in the presence of endogeneity. Specifically, this package includes James Heckman's classical simultaneous equation models-the sample selection model for outcome selection bias and hybrid model with structural shift for endogenous treatment. For more information, see the seminal paper of Heckman (1978) <DOI:10.3386/w0177> in which the details of these models are provided. This package accommodates repeated measures on subjects with a working independence approach. The hybrid model further accommodates treatment effect modification.
	"""
	
	cran = "endogenous" 

	version("1.0", md5="47ffe67546b33d0c07e688dc0dbc2523")

	depends_on("r-mvtnorm", type=("build", "run"))
