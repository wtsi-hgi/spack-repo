# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RRepello(RPackage):
	"""Reports from Trello in R

	Creates reports from Trello, a collaborative, project organization 
             and list-making application. <https://trello.com/>
             Reports are created by comparing individual Trello board
             cards from two different points in time and documenting any changes made
             to the cards.
	"""
	
	homepage = "https://github.com/thomasgstewart/repello"
	cran = "repello" 

	version("1.0.1", md5="4192fb848850af12155a484d8021c9b1")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-httr", type=("build", "run"))
	depends_on("r-dplyr", type=("build", "run"))
	depends_on("r-stringr", type=("build", "run"))
