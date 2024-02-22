# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RSanitizers(RPackage):
	"""C/C++ Source Code to Trigger Address and Undefined Behaviour
Sanitizers

	Recent gcc and clang compiler versions provide functionality to
 test for memory violations and other undefined behaviour; this is often 
 referred to as "Address Sanitizer" (or 'ASAN') and "Undefined Behaviour 
 Sanitizer" ('UBSAN'). The Writing R Extension manual describes this in some
 detail in Section 4.3 title "Checking Memory Access".

   This feature has to be enabled in the corresponding binary, eg in R, which
 is somewhat involved as it also required a current compiler toolchain which 
 is not yet widely available, or in the case of Windows, not available at all
 (via the common Rtools mechanism).

   As an alternative, pre-built Docker containers such as the Rocker container
 'r-devel-san' or the multi-purpose container 'r-debug' can be used.

   This package then provides a means of testing the compiler setup as the
 known code failures provides in the sample code here should be detected
 correctly, whereas a default build of R will let the package pass.

   The code samples are based on the examples from the Address Sanitizer
 Wiki at <https://github.com/google/sanitizers/wiki>.
	"""
	
	homepage = "https://github.com/eddelbuettel/sanitizers"
	cran = "sanitizers" 

	version("0.1.1", md5="2263341fa7514927e6e680216be3af83")

