# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPcl(RPackage):
	"""Proximal Causal Learning

	We fit causal models using proxies. We implement two stage proximal least squares estimator. E.J. Tchetgen Tchetgen, A. Ying, Y. Cui, X. Shi, and W. Miao. (2020). An Introduction to Proximal Causal Learning. arXiv e-prints, arXiv-2009 <arXiv:2009.10982>.
	"""
	
	cran = "PCL" 

	version("1.0", md5="8a217283eb0986618d8e197eb6c64e3f")

	depends_on("r@4:", type=("build", "run"))
