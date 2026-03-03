# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RDprint(RPackage):
	"""Print Tabular Data to Graphics Device

	Provides a generalized method for printing tabular data within 
	the R environment in order to make the process of presenting high quality 
	tabular output seamless for the user.  Output is directed to the R graphics 
	device so that tables can be exported to any file format supported by the 
	graphics device. Utilizes a formula interface to specify the contents of 
	tables often found in manuscripts or business reports.  In addition, formula 
	interface provides inline formatting of the numeric cells of a table and 
	renaming column labels.
	"""
	
	cran = "dprint" 

	version("0.0.4", md5="a0c018575a3618a5d086646f81abb7a9")

	depends_on("r@3:", type=("build", "run"))
