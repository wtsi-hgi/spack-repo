# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDoem(RPackage):
	"""The Distributed Online Expectation Maximization Algorithms to
Solve Parameters of Poisson Mixture Models

	The distributed online expectation maximization algorithms are used to solve parameters of Poisson mixture models. The philosophy of the package is described in Guo, G. (2022) <doi:10.1080/02664763.2022.2053949>.
	"""
	
	cran = "DOEM" 

	version("0.0.0.1", md5="c909717e77de98a67260e0d988913259")

	depends_on("r@3.5:", type=("build", "run"))
