# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RPsycho(RPackage):
	"""Efficient and Publishing-Oriented Workflow for Psychological
Science

	The main goal of the psycho package is to provide tools for psychologists, neuropsychologists and neuroscientists, 
   to facilitate and speed up the time spent on data analysis. It aims at supporting best practices and tools to format the output 
   of statistical methods to directly paste them into a manuscript, ensuring statistical reporting standardization and conformity.
	"""
	
	homepage = "https://github.com/neuropsychology/psycho.R"
	cran = "psycho" 

	version("0.6.1", md5="1a450f3edf7b367e4ffb692778493954")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-scales", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
	depends_on("r-ggplot2", type=("build", "run"))
	depends_on("r-insight", type=("build", "run"))
	depends_on("r-bayestestr", type=("build", "run"))
	depends_on("r-parameters", type=("build", "run"))
	depends_on("r-effectsize", type=("build", "run"))
