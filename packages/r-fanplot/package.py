# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFanplot(RPackage):
	"""Visualisation of Sequential Probability Distributions Using Fan
Charts

	Visualise sequential distributions using a range of plotting
    styles. Sequential distribution data can be input as either simulations or
    values corresponding to percentiles over time. Plots are added to
    existing graphic devices using the fan function. Users can choose from four
    different styles, including fan chart type plots, where a set of coloured
    polygon, with shadings corresponding to the percentile values are layered
    to represent different uncertainty levels. Full details in R Journal article; Abel (2015) <doi:10.32614/RJ-2015-002>.
	"""
	
	homepage = "http://guyabel.github.io/fanplot/"
	cran = "fanplot" 

	version("4.0.0", md5="f3c5675b177d5a6c3ede95137d1d8e48")

	depends_on("r@2.10:", type=("build", "run"))
