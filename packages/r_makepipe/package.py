# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMakepipe(RPackage):
	"""Pipeline Tools Inspired by 'GNU Make'

	A suite of tools for transforming an existing workflow into a
    self-documenting pipeline with very minimal upfront costs. Segments of
    the pipeline are specified in much the same way a 'Make' rule is, by
    declaring an executable recipe (which might be an R script), along
    with the corresponding targets and dependencies. When the entire
    pipeline is run through, only those recipes that need to be executed
    will be. Meanwhile, execution metadata is captured behind the scenes
    for later inspection.
	"""
	
	homepage = "https://kinto-b.github.io/makepipe/"
	cran = "makepipe" 

	version("0.2.1", md5="4b31ea63eef8ab18003af89d74b2edc2")

	depends_on("r-cli", type=("build", "run"))
	depends_on("r-nomnoml", type=("build", "run"))
	depends_on("r-r6", type=("build", "run"))
	depends_on("r-roxygen2", type=("build", "run"))
