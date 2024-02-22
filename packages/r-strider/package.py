# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RStrider(RPackage):
	"""Strided Iterator and Range

	The strided iterator adapts multidimensional buffers to work with 
  the C++ standard library and range-based for-loops. Given a pointer or iterator
  into a multidimensional data buffer, one can generate an iterator range using
  make_strided to construct strided versions of the standard library's begin and
  end. For constructing range-based for-loops, a strided_range class is provided.
  These help authors to avoid integer-based indexing, which in some cases can impede
  algorithm performance and introduce indexing errors. This library exists
  primarily to expose the header file to other R projects.
	"""
	
	homepage = "https://github.com/thk686/strider"
	cran = "strider" 

	version("1.3", md5="e4cf42de624cc3aaf8c2949251325281")

	depends_on("r-rcpp", type=("build", "run"))
	depends_on("r-bh", type=("build", "run"))
