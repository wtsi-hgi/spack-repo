# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFselector(RPackage):
	"""Selecting Attributes

	Functions for selecting attributes from a given
    dataset. Attribute subset selection is the process of identifying and
    removing as much of the irrelevant and redundant information as
    possible.
	"""
	
	homepage = "https://github.com/larskotthoff/fselector"
	cran = "FSelector" 

	version("0.34", md5="a6622536232fa7c2e79543424df4b650")

	depends_on("r-digest", type=("build", "run"))
	depends_on("r-entropy", type=("build", "run"))
	depends_on("r-randomforest", type=("build", "run"))
	depends_on("r-rweka", type=("build", "run"))
