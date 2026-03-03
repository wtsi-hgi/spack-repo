# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RIsatabr(RPackage):
	"""Implementation for the ISA Abstract Model

	ISA is a metadata framework to manage an increasingly diverse set 
    of life science, environmental and biomedical experiments. In isatabr 
    methods for reading, modifying and writing of files in the ISA-Tab format
    are implemented. It also contains methods for processing assay data.
	"""
	
	homepage = "https://github.com/Biometris/isatabr/"
	cran = "isatabr" 

	version("1.0.1", md5="f1f138feac031b5e616590927ad5a607")

