# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RHdfqlr(RPackage):
	"""Interface to 'HDFql' API

	Provides an interface to 'HDFql' <https://www.hdfql.com/> 
    and helper functions for reading data from and writing data to 'HDF5' files. 'HDFql' 
    provides a high-level language for managing 'HDF5' data that is platform independent.
    For more information, see the reference manual 
    <https://www.hdfql.com/resources/HDFqlReferenceManual.pdf>.
	"""
	
	cran = "hdfqlr" 

	version("0.6-2", md5="0b1b4e3c38cfae64315f006de8e49ac7")

	depends_on("r@3.4:", type=("build", "run"))
