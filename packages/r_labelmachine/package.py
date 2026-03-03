# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RLabelmachine(RPackage):
	"""Make Labeling of R Data Sets Easy

	Assign meaningful labels to data frame columns.
    'labelmachine' manages your label assignment rules in 'yaml' files
    and makes it easy to use the same labels in multiple projects.
	"""
	
	homepage = "https://a-maldet.github.io/labelmachine"
	cran = "labelmachine" 

	version("1.0.0", md5="07c8bcd768a3876540f5fb175db64215")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-yaml@2.2:", type=("build", "run"))
