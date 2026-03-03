# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFilenamer(RPackage):
	"""Easy Management of File Names

	Create descriptive file names with ease. New file names are
    automatically (but optionally) time stamped and placed in date stamped
    directories. Streamline your analysis pipeline with input and output file
    names that have informative tags and proper file extensions.
	"""
	
	homepage = "https://bitbucket.org/djhshih/filenamer"
	cran = "filenamer" 

	version("0.2.3", md5="405f2a494eabbb2bcc324e76b7f35d2f")

