# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAke(RPackage):
	"""Associated Kernel Estimations

	Continuous and discrete (count or categorical) estimation of density, probability mass function (p.m.f.) and regression functions are performed using  associated kernels. The cross-validation  technique and the local Bayesian procedure are also implemented for bandwidth selection.
	"""
	
	homepage = "www.r-project.org"
	cran = "Ake" 

	version("1.0.1", md5="94d0744c7215c99c6d3bb6fd677c6b5c")

