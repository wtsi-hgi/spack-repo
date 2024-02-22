# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RResult(RPackage):
	"""Result Type for Safely Handling Operations that can Succeed or
Fail

	Allows wrapping values in success() and failure() types to capture 
    the result of operations, along with any status codes. Risky expressions can be 
    wrapped in as_result() and functions wrapped in result() to catch errors
    and assign the relevant result types. Monadic functions can be bound together 
    as pipelines or transaction scripts using then_try(), to gracefully handle 
    errors at any step.
	"""
	
	homepage = "https://github.com/soumyaray/result"
	cran = "result" 

	version("0.1.0", md5="8e437177d6ad14c878582c55faaaaad0")

