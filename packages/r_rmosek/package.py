# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRmosek(RPackage):
	"""The R to MOSEK Optimization Interface

	This is a meta-package designed to support the
        installation of Rmosek (>= 6.0) and bring the optimization
        facilities of MOSEK (>= 6.0) to the R-language. The interface
        supports large-scale optimization of many kinds: Mixed-integer
        and continuous linear, second-order cone, exponential cone and
        power cone optimization, as well as continuous semidefinite
        optimization. Rmosek and the R-language are open-source
        projects. MOSEK is a proprietary product, but unrestricted
        trial and academic licenses are available.
	"""
	
	homepage = "http://www.mosek.com/"
	cran = "Rmosek" 

	version("1.3.5", md5="f20d7ce06492ceaeadd0053d8eaf8a26")

