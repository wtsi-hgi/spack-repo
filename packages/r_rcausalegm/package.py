# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRcausalegm(RPackage):
	"""A General Causal Inference Framework by Encoding Generative
Modeling

	CausalEGM is a general causal inference framework for estimating causal effects by encoding generative modeling, which can be applied in both discrete and continuous treatment settings. A description of the methods is given in Liu (2022) <arXiv:2212.05925>.
	"""
	
	homepage = "https://github.com/SUwonglab/CausalEGM"
	cran = "RcausalEGM" 

	version("0.3.3", md5="0f05ec41360061dff40ea4f184aca74a")

	depends_on("r@3.6:", type=("build", "run"))
	depends_on("r-reticulate", type=("build", "run"))
