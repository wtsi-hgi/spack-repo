# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMsgr(RPackage):
	"""Extends Messages, Warnings and Errors by Adding Levels and Log
Files

	Provides new functions info(), warn() and error(), similar to message(),
    warning() and stop() respectively. However, the new functions can have a 'level'
    associated with them, so that when executed the global level option determines whether
    they are shown or not. This allows debug modes, outputting more information. The can also
    output all messages to a log file.
	"""
	
	homepage = "https://github.com/ChadGoymer/msgr"
	cran = "msgr" 

	version("1.1.2", md5="b6800b8d7eee61cfedcc8a9420ba588b")

	depends_on("r-rlang", type=("build", "run"))
	depends_on("r-purrr", type=("build", "run"))
