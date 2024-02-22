# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdvdif4(RPackage):
	"""Solving 1D Advection Bi-Flux Diffusion Equation

	This software solves an Advection Bi-Flux Diffusive Problem using the Finite Difference Method FDM. Vasconcellos, J.F.V., Marinho, G.M., Zanni, J.H., 2016, Numerical analysis of an anomalous diffusion with a bimodal flux distribution. <doi:10.1016/j.rimni.2016.05.001>. Silva, L.G., Knupp, D.C., Bevilacqua, L., Galeao, A.C.N.R., Silva Neto, A.J., 2014, Formulation and solution of an Inverse Anomalous Diffusion Problem with Stochastic Techniques. <doi:10.5902/2179460X13184>. In this version, it is possible to include a source as a function depending on space and time, that is, s(x,t).
	"""
	
	cran = "AdvDif4" 

	version("0.7.18", md5="80bd16d35e38f761d1898e2d6dcb945e", url="https://cran.r-project.org/src/contrib/AdvDif4_0.7.18.tar.gz")

