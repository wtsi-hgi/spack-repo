# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class ROccupationmeasurement(RPackage):
	"""Interactively Measure Occupations in Interviews and Beyond

	Perform interactive occupation coding during interviews as
    described in Peycheva, D., Sakshaug, J., Calderwood, L. (2021) <doi:10.2478/jos-2021-0042>
    and Schierholz, M., Gensicke, M., Tschersich, N., Kreuter, F. (2018) <doi:10.1111/rssa.12297>.
    Generate suggestions for occupational categories based on free text
    input, with pre-trained machine learning models in German and a ready-to-use
    shiny application provided for quick and easy data collection.
	"""
	
	homepage = "https://occupationMeasurement.github.io/occupationMeasurement/"
	cran = "occupationMeasurement" 

	version("0.3.2", md5="57e60db8fbfb86079f296d0606ea597d")

	depends_on("r@4.1:", type=("build", "run"))
	depends_on("r-data-table@1.14.2:", type=("build", "run"))
	depends_on("r-digest", type=("build", "run"))
	depends_on("r-shiny@1.7.1:", type=("build", "run"))
	depends_on("r-stringdist@0.9.8:", type=("build", "run"))
	depends_on("r-stringr@1.4:", type=("build", "run"))
	depends_on("r-text2vec@0.6.1:", type=("build", "run"))
	depends_on("r-tm@0.7.8:", type=("build", "run"))
