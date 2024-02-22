# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RBardr(RPackage):
	"""Complete Works of William Shakespeare in Tidy Format

	Provides R data structures for Shakespeare's complete works, 
  as provided by Project Gutenberg <https:www.gutenberg.org/ebooks/100>.
	"""
	
	cran = "bardr" 

	version("0.0.9", md5="2b2ba6908706db06e3ee176ecb93d853")

	depends_on("r@3.6:", type=("build", "run"))
