# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSecp(RPackage):
	"""Statistical Estimation of Cluster Parameters

	Estimating parameters of site clusters on 2D & 3D square lattice with various lattice sizes, relative fractions of open sites (occupation probability), iso- & anisotropy, von Neumann & Moore (1,d)-neighborhoods, described by Moskalev P.V. et al. (2011) <arXiv:1105.2334v1>.
	"""
	
	cran = "SECP" 

	version("0.1.5", md5="b417b60920ee599d46a9fc1e6a64a9b4")

	depends_on("r-spsl", type=("build", "run"))
