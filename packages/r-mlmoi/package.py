# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMlmoi(RPackage):
	"""Estimating Frequencies, Prevalence and Multiplicity of Infection

	The implemented methods reach out to scientists that seek to estimate multiplicity of infection (MOI) and lineage (allele) frequencies and prevalences at molecular markers using the maximum-likelihood method described in Schneider (2018) <doi:10.1371/journal.pone.0194148>, and Schneider and Escalante (2014) <doi:10.1371/journal.pone.0097899>. Users can import data from Excel files in various formats, and perform maximum-likelihood estimation on the imported data by the package's moimle() function.
	"""
	
	cran = "MLMOI" 

	version("0.1.2", md5="0183a685542ada1676edb5becffaaafc")

	depends_on("r@4.3:", type=("build", "run"))
	depends_on("r-openxlsx@4.2.5.2:", type=("build", "run"))
	depends_on("r-rdpack@2.6:", type=("build", "run"))
	depends_on("r-rmpfr@0.9.3:", type=("build", "run"))
