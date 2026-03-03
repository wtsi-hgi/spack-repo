# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCpmr(RPackage):
	"""Connectome Predictive Modelling in R

	Connectome Predictive Modelling (CPM) (Shen et al. (2017)
    <doi:10.1038/nprot.2016.178>) is a method to predict individual
    differences in behaviour from brain functional connectivity. 'cpmr'
    provides a simple yet efficient implementation of this method.
	"""
	
	homepage = "https://github.com/psychelzh/cpmr"
	cran = "cpmr" 

	version("0.0.8", md5="64144a679c01f3f86b46743a0489b99f")

	depends_on("r-rfast", type=("build", "run"))
