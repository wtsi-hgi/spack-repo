# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RTextutils(RPackage):
	"""Utilities for Handling Strings and Text

	Utilities for handling character vectors
  that store human-readable text (either plain or with
  markup, such as HTML or LaTeX). The package provides,
  in particular, functions that help with the
  preparation of plain-text reports, e.g. for expanding
  and aligning strings that form the lines of such
  reports. The package also provides generic functions for
  transforming R objects to HTML and to plain text.
	"""
	
	homepage = "http://enricoschumann.net/R/packages/textutils/"
	cran = "textutils" 

	version("0.4-1", md5="a8415833c5f8c7cb6b8d0c4e42bff358")
	version("0.3-2", md5="6679d229d5188d6d8657dcb29bfa6360")

