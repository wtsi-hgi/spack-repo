# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBackpipe(RPackage):
	"""Backward Pipe (Right-to-Left) Operator

	Provides a backward-pipe operator for 'magrittr' (%<%) or 
    'pipeR' (%<<%) that allows for a performing operations from right-to-left. 
    This allows writing more legible code where right-to-left ordering is 
    natural. This is common with hierarchies and nested structures such as 
    trees, directories or markup languages (e.g. HTML and XML). 
    The package also includes a R-Studio add-in that can be bound to a keyboard 
    shortcut. 
	"""
	
	homepage = "https://github.com/decisionpatterns/backpipe"
	cran = "backpipe" 

	version("0.2.3", md5="6e41c13adb2f7d18454722156c4150c2")

	depends_on("r@3.1:", type=("build", "run"))
