# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScriptname(RPackage):
	"""Determine a Script's Filename from Within the Script Itself

	A small set of functions wrapping up the call stack and command
  line inspection needed to determine a running script's filename from
  within the script itself.
	"""
	
	homepage = "https://github.com/MullinsLab/scriptName"
	cran = "scriptName" 

	version("1.0.1", md5="02aada56f398a9afd8a71820323902cf")

	depends_on("r-rlang@0.1:", type=("build", "run"))
	depends_on("r-purrr@0.2.3:", type=("build", "run"))
