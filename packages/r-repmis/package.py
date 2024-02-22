# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepmis(RPackage):
	"""Miscellaneous Tools for Reproducible Research

	Tools to load 'R' packages
    and automatically generate BibTeX files citing them as well as load and
    cache plain-text and 'Excel' formatted data stored on 'GitHub', and
    from other sources.
	"""
	
	homepage = "http://cran.r-project.org/package=repmis"
	cran = "repmis" 

	version("0.5", md5="0ccad72f6daec08266af1ae5676c8496")

	depends_on("r@3:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-plyr", type=("build", "run"))
	depends_on("r-r-cache", type=("build", "run"))
