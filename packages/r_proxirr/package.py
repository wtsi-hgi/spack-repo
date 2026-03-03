# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProxirr(RPackage):
	"""Alpha and Beta Proximity to Irreplaceability

	Functions to measure Alpha and Beta Proximity to Irreplaceability.
  The methods for Alpha and Beta irreplaceability were first described in:
    Baisero D., Schuster R. & Plumptre A.J.
    Redefining and Mapping Global Irreplaceability.
    Conservation Biology 2021;1-11.
    <doi:10.1111/cobi.13806>.
	"""
	
	cran = "proxirr" 

	version("0.4", md5="3e4384b49a4abb5858f69c3b716ec9cb")

