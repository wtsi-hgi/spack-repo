# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSarpMoodle(RPackage):
	"""XML Output Functions for Easy Creation of Moodle Questions

	Provides a set of basic functions for creating Moodle XML
 output files suited for importing questions in Moodle (a learning
 management system, see <https://moodle.org/> for more information).
	"""
	
	cran = "SARP.moodle" 

	version("1.0.4", md5="5ecfc57f6b94a5f2df2cc167ac535c9b")

	depends_on("r-base64enc", type=("build", "run"))
