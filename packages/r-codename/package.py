# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCodename(RPackage):
	"""Generation of Code Names for Organizations, People, Projects,
and Whatever Else

	This creates code names that a user can consider for their organizations, their projects, themselves, people
    in their organizations or projects, or whatever else. The user can also supply a numeric seed (and even a character seed)
    for maximum reproducibility. Use is simple and the code names produced come in various types too, contingent on what the
    user may be desiring as a code name or nickname.
	"""
	
	homepage = "https://github.com/svmiller/codename"
	cran = "codename" 

	version("0.5.0", md5="fa7105eb3ae81198d9a170835fb87548")

	depends_on("r@3.5:", type=("build", "run"))
