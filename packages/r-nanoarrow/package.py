# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RNanoarrow(RPackage):
	"""Interface to the 'nanoarrow' 'C' Library

	Provides an 'R' interface to the 'nanoarrow' 'C' library and the
  'Apache Arrow' application binary interface. Functions to import and
  export 'ArrowArray', 'ArrowSchema', and 'ArrowArrayStream' 'C' structures
  to and from 'R' objects are provided alongside helpers to facilitate zero-copy
  data transfer among 'R' bindings to libraries implementing the 'Arrow' 'C'
  data interface.
	"""
	
	homepage = "https://github.com/apache/arrow-nanoarrow"
	cran = "nanoarrow" 

	version("0.4.0", md5="d5251d4b4e2fa25bab6c404ad647ec63")

