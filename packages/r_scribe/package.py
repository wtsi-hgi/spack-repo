# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScribe(RPackage):
	"""Command Argument Parsing

	A base dependency solution with basic argument parsing for use with
    'Rscript'.
	"""
	
	homepage = "https://jmbarbone.github.io/scribe/"
	cran = "scribe" 

	version("0.3.0", md5="e8c3e886e8f3606a1f0462d04b22c109")

	depends_on("r@3.6:", type=("build", "run"))
