# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBayesrepdesign(RPackage):
	"""Bayesian Design of Replication Studies

	Provides functionality for determining the sample size of replication studies using Bayesian design approaches in the normal-normal hierarchical model (Pawel et al., 2022) <doi:10.48550/arXiv.2211.02552>.
	"""
	
	homepage = "https://github.com/SamCH93/BayesRepDesign"
	cran = "BayesRepDesign" 

	version("0.42", md5="7b2c4f997e3fb9b17f16678bc8be0f0a")

	depends_on("r-lamw", type=("build", "run"))
