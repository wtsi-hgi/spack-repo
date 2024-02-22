# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROca(RPackage):
	"""Optimal Capital Allocations

	Computes optimal capital allocations based on some standard principles such as Haircut, Overbeck type II and the Covariance Allocation Principle. It also provides some shortcuts for obtaining the Value at Risk and the Expectation Shortfall, using both the normal and the t-student distribution, see Urbina and Guillén (2014)<doi:10.1016/j.eswa.2014.05.017> and Urbina (2013)<http://hdl.handle.net/2099.1/19443>.
	"""
	
	cran = "OCA" 

	version("0.5", md5="d6ba6b2f3bc6aff14b94fdf0550b164c")

	depends_on("r-mathjaxr", type=("build", "run"))
