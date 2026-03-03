# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRoger(RPackage):
	"""Automated Grading of R Scripts

	Tools for grading the coding style and documentation of R
  scripts. This is the R component of Roger the Omni Grader, an
  automated grading system for computer programming projects based on
  Unix shell scripts; see <https://gitlab.com/roger-project>. The
  package also provides an R interface to the shell scripts. Inspired by
  the lintr package.
	"""
	
	homepage = "https://roger-project.gitlab.io"
	cran = "roger" 

	version("1.5-1", md5="adf0159f5899f6b181353484995fb7b8")

	depends_on("r@4:", type=("build", "run"))
