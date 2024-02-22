# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RAdditivedea(RPackage):
	"""Additive Data Envelopment Analysis Models

	Provides functions for calculating efficiency with two types of additive Data Envelopment Analysis models: (i) Generalized Efficiency Measures: unweighted additive model (Cooper et al., 2007 <doi:10.1007/978-0-387-45283-8>), Range Adjusted Measure (Cooper et al., 1999, <doi:10.1023/A:1007701304281>), Bounded Adjusted Measure (Cooper et al., 2011 <doi:10.1007/s11123-010-0190-2>), Measure of Inefficiency Proportions (Cooper et al., 1999 <doi:10.1023/A:1007701304281>), and the Lovell-Pastor Measure (Lovell and Pastor, 1995 <doi:10.1016/0167-6377(95)00044-5>); and (ii) the Slacks-Based Measure (Tone, 2001 <doi:10.1016/S0377-2217(99)00407-5>). The functions provide several options: (i) constant and variable returns to scale; (ii) fixed (non-controllable) inputs and/or outputs; (iii) bounding the slacks so that unrealistically large slack values are avoided; and (iv) calculating the efficiency of specific Decision-Making Units (DMUs), rather than of the whole sample. Package additiveDEA also provides a function for reducing computation time when datasets are large.
	"""
	
	homepage = "https://www.r-project.org"
	cran = "additiveDEA" 

	version("1.1", md5="93ce921c8a14afa6deb4626dedbd409c")

	depends_on("r@3.1:", type=("build", "run"))
	depends_on("r-lpsolveapi", type=("build", "run"))
	depends_on("r-benchmarking", type=("build", "run"))
