# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlowr(RPackage):
	"""Streamlining Design and Deployment of Complex Workflows

	This framework allows you to design and implement complex
    pipelines, and deploy them on your institution's computing cluster. This has
    been built keeping in mind the needs of bioinformatics workflows. However, it is
    easily extendable to any field where a series of steps (shell commands) are to
    be executed in a (work)flow.
	"""
	
	homepage = "https://github.com/flow-r/flowr"
	cran = "flowr" 

	version("0.9.11", md5="d6c2b212b56f63608d2f24b5010554f4")

	depends_on("r@3.3:", type=("build", "run"))
	depends_on("r-params@0.7:", type=("build", "run"))
	depends_on("r-diagram", type=("build", "run"))
	depends_on("r-whisker", type=("build", "run"))
	depends_on("r-readr", type=("build", "run"))
