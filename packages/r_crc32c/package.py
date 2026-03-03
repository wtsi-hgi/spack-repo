# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RCrc32c(RPackage):
	"""Cyclic Redundancy Check with CPU-Specific Acceleration

	Hardware-based support for 'CRC32C' cyclic redundancy checksum function
  is made available for 'x86_64' systems with 'SSE2' support as well as for 'arm64', 
  and detected at build-time via 'cmake' with a software-based fallback.  This
  functionality is exported at the 'C'-language level for use by other packages.
  'CRC32C' is described in 'RFC 3270' at <https://datatracker.ietf.org/doc/html/rfc3720>
  and is based on 'Castagnoli et al' <doi:10.1109/26.231911>.
	"""
	
	homepage = "https://github.com/google/crc32c"
	cran = "crc32c" 

	version("0.0.2", md5="25f62f381d448f64edb4f8f4eed8f017")

	depends_on("r-tidycpp", type=("build", "run"))
	depends_on("cmake", type=("build", "link", "run"))
