# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLuzlogr(RPackage):
	"""Lightweight Logging for R Scripts

	Provides flexible but lightweight logging facilities for R scripts.
    Supports priority levels for logs and messages, flagging messages, capturing
    script output, switching logs, and logging to files or connections.
	"""
	
	cran = "luzlogr" 

	version("0.2.0", md5="a7036a3b1ceb039ea972ffbfd9492a8d")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-assertthat@0.1:", type=("build", "run"))
