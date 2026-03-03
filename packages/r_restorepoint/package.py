# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRestorepoint(RPackage):
	"""Debugging with Restore Points

	Debugging with restore points instead of break points. A restore
    point stores all local variables when called inside a function. The stored
    values can later be retrieved and evaluated in a modified R console that
    replicates the function's environment. To debug step by step, one can simply
    copy & paste the function body from the R script. Particularly convenient
    in combination with "RStudio". See the "Github" page inst/vignettes for a
    tutorial.
	"""
	
	homepage = "https://github.com/skranz/restorepoint"
	cran = "restorepoint" 

	version("0.2", md5="ac265f803507c83ea72027130c58d978")

