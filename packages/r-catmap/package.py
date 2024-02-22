# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCatmap(RPackage):
	"""Case-Control and TDT Meta-Analysis Package

	Although many software tools can perform meta-analyses on genetic case-control data,
    none of these apply to combined case-control and family-based (TDT) studies. This package conducts
    fixed-effects (with inverse variance weighting) and random-effects [DerSimonian and Laird (1986)
    <DOI:10.1016/0197-2456(86)90046-2>] meta-analyses on combined genetic data. Specifically, this package
    implements a fixed-effects model [Kazeem and Farrall (2005) <DOI:10.1046/j.1529-8817.2005.00156.x>]
    and a random-effects model [Nicodemus (2008) <DOI:10.1186/1471-2105-9-130>] for combined studies.
	"""
	
	homepage = "http://github.com/tpq/catmap"
	cran = "catmap" 

	version("1.6.4", md5="17f0be70c5e7c728b3505db438db9417")

	depends_on("r@2.10:", type=("build", "run"))
	depends_on("r-forestplot", type=("build", "run"))
	depends_on("r-metafor", type=("build", "run"))
