# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAsymptor(RPackage):
	"""Estimate Asymptomatic Cases via Capture/Recapture Methods

	Estimate the lower and upper bound of asymptomatic cases in an 
    epidemic using the capture/recapture methods from Böhning et al. (2020) 
    <doi:10.1016/j.ijid.2020.06.009> and Rocchetti et al. (2020)
    <doi:10.1101/2020.07.14.20153445>. Note there is currently some discussion
    about the validity of the methods implemented in this package. You should
    read carefully the original articles, alongside this answer from Li et al.
    (2022) <doi:10.48550/arXiv.2209.11334> before using this package in your
    project.
	"""
	
	homepage = "https://hugogruson.fr/asymptor/"
	cran = "asymptor" 

	version("1.1.0", md5="31677b65dc1dcc8cc75b898eee6feea4")

	depends_on("r@3.5:", type=("build", "run"))
