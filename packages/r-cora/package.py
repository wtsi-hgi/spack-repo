# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCora(RPackage):
	"""Cora Data for Entity Resolution

	Duplicated publication data (pre-processed and formatted) for entity resolution. This data set contains a total of 1879 records. The following variables are included in the data set: id, title, book title, authors, address, date, year, editor, journal, volume, pages, publisher, institution, type, tech, note. The data set has a respective gold data set that provides information on which records match based on id. 
	"""
	
	homepage = "https://github.com/resteorts/cora"
	cran = "cora" 

	version("0.1.0", md5="474841744a8816da88ed2c25e11272c4")

	depends_on("r@3.4:", type=("build", "run"))
