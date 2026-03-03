# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RFlobr(RPackage):
	"""Convert Files to and from Binary Objects (BLOBs)

	Converts files to and from flobs.  A flob is a file that was
    read into binary in integer-mode as little endian, saved as the single
    element of a named list (where the name is the name of the original
    file) and then serialized before being coerced into a blob.  Flobs are
    useful for writing and reading files to and from databases.
	"""
	
	homepage = "https://github.com/poissonconsulting/flobr"
	cran = "flobr" 

	version("0.2.3", md5="ddc82e9e6d05198c609d3874181b38e0")

	depends_on("r@3.5:", type=("build", "run"))
	depends_on("r-blob", type=("build", "run"))
	depends_on("r-chk", type=("build", "run"))
	depends_on("r-lifecycle", type=("build", "run"))
