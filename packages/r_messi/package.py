# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMessi(RPackage):
	"""Mediation Analysis with External Summary-Level Information on
Total Effect

	Fits the hard constraint, soft constraint, and unconstrained models 
    in Boss et al. (2023) <arXiv:2306.17347> for mediation analyses with external summary-level 
    information on the total effect.
	"""
	
	homepage = "https://github.com/umich-cphds/messi"
	cran = "messi" 

	version("0.1.1", md5="7e897d74b0eda654a8d05d72a15b570e")

	depends_on("r@3.6.2:", type=("build", "run"))
	depends_on("r-mass", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-patchwork", type=("build", "run"))
	depends_on("r-progress", type=("build", "run"))
