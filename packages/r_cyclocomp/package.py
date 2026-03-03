# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCyclocomp(RPackage):
	"""Cyclomatic Complexity of R Code

	Cyclomatic complexity is a software metric (measurement),
    used to indicate the complexity of a program. It is a quantitative
    measure of the number of linearly independent paths through a program's
    source code. It was developed by Thomas J. McCabe, Sr. in 1976.
	"""
	
	homepage = "https://github.com/gaborcsardi/cyclocomp"
	cran = "cyclocomp" 

	version("1.1.1", md5="8e8d8ea42dea69952eecae52d4242e05")

	depends_on("r-callr", type=("build", "run"))
	depends_on("r-crayon", type=("build", "run"))
	depends_on("r-desc", type=("build", "run"))
	depends_on("r-remotes", type=("build", "run"))
	depends_on("r-withr", type=("build", "run"))
