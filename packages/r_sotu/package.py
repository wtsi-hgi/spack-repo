# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSotu(RPackage):
	"""United States Presidential State of the Union Addresses

	The President of the United States is constitutionally obligated to provide
  a report known as the 'State of the Union'. The report summarizes the current challenges
  facing the country and the president's upcoming legislative agenda. While historically
  the State of the Union was often a written document, in recent decades it has always
  taken the form of an oral address to a joint session of the United States Congress.
  This package provides the raw text from every such address with the intention of
  being used for meaningful examples of text analysis in R. The corpus is well suited
  to the task as it is historically important, includes material intended to be read
  and material intended to be spoken, and it falls in the public domain. As the corpus
  spans over two centuries it is also a good test of how well various methods hold up
  to the idiosyncrasies of historical texts. Associated data about each address, such
  as the year, president, party, and format, are also included.
	"""
	
	homepage = "https://github.com/statsmaths/sotu/"
	cran = "sotu" 

	version("1.0.4", md5="23972d0d9dd70ab007a0ddc6fdd9a91c")

	depends_on("r@3.5:", type=("build", "run"))
