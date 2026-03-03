# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RScriptexec(RPackage):
	"""Execute Native Scripts

	Run complex native scripts with a single command, similar to system commands.
	"""
	
	homepage = "https://github.com/sagiegurari/scriptexec"
	cran = "scriptexec" 

	version("0.3.1", md5="4b79461f9956823a3cfa8d4e5a8fb4e7")

	depends_on("r@3.2.3:", type=("build", "run"))
