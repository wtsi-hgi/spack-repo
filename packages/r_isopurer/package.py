# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsopurer(RPackage):
	"""Deconvolution of Tumour Profiles

	Deconvolution of mixed tumour profiles into normal and cancer for each patient, using 
	the ISOpure algorithm in Quon et al. Genome Medicine, 2013 5:29. Deconvolution requires 
	mixed tumour profiles and a set of unmatched "basis" normal profiles.
	"""
	
	cran = "ISOpureR" 

	version("1.1.3", md5="dfb4939e1d12899ec3534c047edd669d")

	depends_on("r@3.1.1:", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-futile-logger", type=("build", "run"))
	depends_on("r-rcppeigen@0.3.2.2:", type=("build", "run"))
