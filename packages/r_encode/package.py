# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REncode(RPackage):
	"""Represent Ordered Lists and Pairs as Strings

	Interconverts between ordered lists and compact string notation.  
 Useful for capturing code lists, and pair-wise codes and decodes, for text storage.
 Analogous to factor levels and labels. Generics encode() and decode()
 perform interconversion, while codes() and decodes() extract components of an encoding.
 The function encoded() checks whether something is interpretable as an encoding.
 If a vector has an encoded 'guide' attribute, as_factor() uses it to coerce to factor.
	"""
	
	cran = "encode" 

	version("0.3.6", md5="e4eab9e766d12d42031c933cadd62ad7")

