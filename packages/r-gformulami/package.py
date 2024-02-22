# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGformulami(RPackage):
	"""G-Formula for Causal Inference via Multiple Imputation

	Implements the G-Formula method for causal inference with time-varying treatments and
  confounders using Bayesian multiple imputation methods, as described by
  Bartlett, Olarte Parra and Daniel (2023) <arXiv:2301.12026>. It creates multiple synthetic imputed
  datasets under treatment regimes of interest using the 'mice' package. These can then be analysed
  using rules developed for analysing multiple synthetic datasets.
	"""
	
	homepage = "https://jwb133.github.io/gFormulaMI/"
	cran = "gFormulaMI" 

	version("1.0.0", md5="43afb78e5734ab7f555a096b781cd338")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-mice", type=("build", "run"))
