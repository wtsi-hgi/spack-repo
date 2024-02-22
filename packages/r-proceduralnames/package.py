# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RProceduralnames(RPackage):
	"""Several Methods for Procedural Name Generation

	A small, dependency-free way to generate random names. Methods 
    provided include the adjective-surname approach of Docker containers 
    ('<https://github.com/moby/moby/blob/master/pkg/namesgenerator/names-generator.go>'),
    and combinations of common English or Spanish words.
	"""
	
	homepage = "https://mikemahoney218.github.io/proceduralnames/"
	cran = "proceduralnames" 

	version("0.2.2", md5="f7fb413e9ef418af747b8e948616fdfa")

	depends_on("r@2.10:", type=("build", "run"))
