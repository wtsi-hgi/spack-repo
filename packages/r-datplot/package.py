# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDatplot(RPackage):
	"""Preparation of Object Dating Ranges for Density Plots (Aoristic
Analysis)

	Converting date ranges into dating 'steps' eases the
    visualization of changes in e.g. pottery consumption, style and other
    variables over time. This package provides tools to process and
    prepare data for visualization and employs the concept of aoristic
    analysis.
	"""
	
	homepage = "https://github.com/lsteinmann/datplot"
	cran = "datplot" 

	version("1.1.1", md5="a4b4fa9c6c622a2a56410919ee41dd3c")

	depends_on("r@3.3:", type=("build", "run"))
