# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRsprite2(RPackage):
	"""Identify Distributions that Match Reported Sample Parameters
(SPRITE)

	The SPRITE algorithm creates possible distributions of discrete responses
    based on reported sample parameters, such as mean, standard deviation and range 
    (Heathers et al., 2018, <doi:10.7287/peerj.preprints.26968v1>). This package implements it, 
    drawing heavily on the code for Nick Brown's 'rSPRITE' Shiny app <https://shiny.ieis.tue.nl/sprite/>. 
    In addition, it supports the modeling of distributions based on multi-item (Likert-type) 
    scales and the use of restrictions on the frequency of particular responses.
	"""
	
	homepage = "https://lukaswallrich.github.io/rsprite2/"
	cran = "rsprite2" 

	version("0.2.1", md5="1642fa3960be3b4c961f6bf989f45fd5", url="https://cran.r-project.org/src/contrib/rsprite2_0.2.1.tar.gz")

	depends_on("r-checkmate", type=("build", "run"))
	depends_on("r-rdpack", type=("build", "run"))
