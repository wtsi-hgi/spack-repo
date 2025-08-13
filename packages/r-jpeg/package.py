# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class RJpeg(RPackage):
	"""Read and write JPEG images.

	This package provides an easy and simple way to read, write and display
	bitmap images stored in the JPEG format. It can read and write both files
	and in-memory raw vectors."""

	cran = "jpeg"
	version("0.1-10", sha256="c8d9f609c3088f91ec4853d6cc0e66511038a465811dea79ca6a0c09519178ca")
	version("0.1-9", sha256="01a175442ec209b838a56a66a3908193aca6f040d537da7838d9368e46913072")
	version("0.1-8.1", sha256="1db0a4976fd9b2ae27a37d3e856cca35bc2909323c7a40724846a5d3c18915a9")
	version("0.1-8", sha256="d032befeb3a414cefdbf70ba29a6c01541c54387cc0a1a98a4022d86cbe60a16")

	depends_on("r@2.9:", type=("build", "run"))
	depends_on("libjpeg", type=("build", "link", "run"))

	# R 4.5 stopped implicitly including <stdbool.h> in its
	# public headers. Older CRAN releases of 'jpeg' expect 'bool'
	# to be available via R headers and fail to compile.
	# Force-include stdbool to maintain compatibility.
	def setup_build_environment(self, env):
		# Limit to R >= 4.5 for minimal surface area
		try:
			from spack.version import Version
			if self.spec.satisfies('^r@4.5:'):
				# R packages honor PKG_CPPFLAGS/PKG_CFLAGS during compilation
				env.append_flags('PKG_CPPFLAGS', '-include stdbool.h')
				env.append_flags('PKG_CFLAGS', '-include stdbool.h')
		except Exception:
			# If anything goes wrong, still attempt to add flags
			env.append_flags('PKG_CPPFLAGS', '-include stdbool.h')
			env.append_flags('PKG_CFLAGS', '-include stdbool.h')
