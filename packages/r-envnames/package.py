# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class REnvnames(RPackage):
	"""Keep Track of User-Defined Environment Names

	Set of functions to keep track and find objects in user-defined environments
    by identifying environments by name --which cannot be retrieved with the built-in function environmentName().
    The package also provides functionality to obtain simplified information about function calling chains
    and to get an object's memory address.
	"""
	
	homepage = "https://github.com/mastropi/envnames"
	cran = "envnames" 

	version("0.4.1", md5="183b6f206fae288514ca77f233fa184c")

