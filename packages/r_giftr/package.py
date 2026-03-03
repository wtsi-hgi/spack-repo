# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RGiftr(RPackage):
	"""GIFT Questions Format Generator from Dataframes

	A framework and functions to create 'MOODLE' quizzes. 'GIFTr' takes dataframe of questions of
    four types: multiple choices, numerical, true or false and short answer questions, and exports a text 
    file formatted in 'MOODLE' GIFT format. You can prepare a spreadsheet in any software and import 
    it into R to generate any number of questions with 'HTML', 'markdown' and 'LaTeX' support.
	"""
	
	homepage = "https://github.com/omarelashkar/GIFTr"
	cran = "GIFTr" 

	version("0.1.0", md5="ee503068dab7112ee5ebe482ec8e4c68")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-glue", type=("build", "run"))
