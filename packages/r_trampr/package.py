# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTrampr(RPackage):
	"""'TRFLP' Analysis and Matching Package for R

	Matching terminal restriction fragment length
        polymorphism ('TRFLP') profiles between unknown samples and a
        database of known samples.  'TRAMPR' facilitates analysis of
        many unknown profiles at once, and provides tools for working
        directly with electrophoresis output through to generating
        summaries suitable for community analyses with R's rich set of
        statistical functions.  'TRAMPR' also resolves the issues of
        multiple 'TRFLP' profiles within a species, and shared 'TRFLP'
        profiles across species.
	"""
	
	homepage = "https://github.com/richfitz/TRAMPR"
	cran = "TRAMPR" 

	version("1.0-10", md5="5399e1c85bb39e2c7094fe2662726260")

	depends_on("r@2.4:", type=("build", "run"))
