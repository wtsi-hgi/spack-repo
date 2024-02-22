# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RWand(RPackage):
	"""Retrieve 'Magic' Attributes from Files and Directories

	'MIME' types are shorthand descriptors for
      file contents and can be determined from "magic"
      bytes in file headers, file contents or intuited
      from file extensions. Tools are provided to
      perform curated "magic" tests as well as mapping
      'MIME' types from a database of over 1,500
      extension mappings.
	"""
	
	homepage = "http://gitlab.com/hrbrmstr/wand"
	cran = "wand" 

	version("0.5.0", md5="5a361ff4b53a0a4b35b07087bf6bfa16")

	depends_on("r@3.2:", type=("build", "run"))
