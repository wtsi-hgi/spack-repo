# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTensorbss(RPackage):
	"""Blind Source Separation Methods for Tensor-Valued Observations

	Contains several utility functions for manipulating tensor-valued data (centering, multiplication from a single mode etc.) and the implementations of the following blind source separation methods for tensor-valued data: 'tPCA', 'tFOBI', 'tJADE', k-tJADE', 'tgFOBI', 'tgJADE', 'tSOBI', 'tNSS.SD', 'tNSS.JD', 'tNSS.TD.JD', 'tPP' and 'tTUCKER'.
	"""
	
	cran = "tensorBSS" 

	version("0.3.8", md5="5d8e517a20fbcbda6b9c6b5515e55129")

	depends_on("r-jade", type=("build", "run"))
	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-fica", type=("build", "run"))
	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-tensor", type=("build", "run"))
	depends_on("r-tsbss", type=("build", "run"))
	depends_on("r-ictest", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-abind", type=("build", "run"))
	depends_on("r-rcpparmadillo", type=("build", "run"))
