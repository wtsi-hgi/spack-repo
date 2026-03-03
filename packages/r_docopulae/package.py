# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDocopulae(RPackage):
	"""Optimal Designs for Copula Models

	A direct approach to optimal designs for copula models based on
    the Fisher information. Provides flexible functions for building joint PDFs,
    evaluating the Fisher information and finding optimal designs. It includes an
    extensible solution to summation and integration called 'nint', functions for
    transforming, plotting and comparing designs, as well as a set of tools for
    common low-level tasks.
	"""
	
	homepage = "http://www.tandfonline.com/doi/full/10.1080/02331888.2015.1111892"
	cran = "docopulae" 

	version("0.4.0", md5="de482eff1b0adef85df338236240b1f5")

	depends_on("r@3.1.2:", type=("build", "run"))
