# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RMeditations(RPackage):
	"""Prints a Random Quote from Marcus Aurelius' Book Meditations

	Prints a random quote from Marcus Aurelius' book Meditations.
	"""
	
	homepage = "https://github.com/jacobkap/meditations"
	cran = "meditations" 

	version("1.0.1", md5="fbf4ea6cd88401ea8f1e2932d003f1ae")

	depends_on("r@2.10:", type=("build", "run"))
