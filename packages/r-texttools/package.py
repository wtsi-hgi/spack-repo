# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTexttools(RPackage):
	"""Functions for Text Cleansing and Text Analysis

	A framework for text cleansing and analysis. Conveniently prepare and process large amounts of text for analysis. 
  Includes various metrics for word counts/frequencies that scale efficiently. Quickly 
  analyze large amounts of text data using a text.table (a data.table created with one word (or unit of text analysis) per row, similar to the tidytext format). 
  Offers flexibility to efficiently work with text data stored in vectors as well as text data formatted as a text.table.
	"""
	
	cran = "textTools" 

	version("0.1.0", md5="73fb1ff1b48be089024f4b53ba65f1a0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-data-table", type=("build", "run"))
